import os
from typing import Optional
from fastapi import FastAPI, HTTPException, Header, status
from pydantic import BaseModel

from tokenizer import _build_analyzer, tokenize_text
from vault import Vault

app = FastAPI(title="PII Tokenization Service")

INTERNAL_VAULT_KEY = os.getenv("INTERNAL_VAULT_KEY", "tessera-internal-vault-secret-key-2026")

# Created once when the server starts, reused for every request.
_analyzer = _build_analyzer()
_vault = Vault()


class TokenizeRequest(BaseModel):
    text: str


class TokenizeResponse(BaseModel):
    tokenized_text: str


class DetokenizeRequest(BaseModel):
    token: str


class DetokenizeResponse(BaseModel):
    token: str
    real_value: str
    on_watchlist: bool


@app.post("/tokenize", response_model=TokenizeResponse)
def tokenize(request: TokenizeRequest) -> TokenizeResponse:
    """Takes raw text, returns the same text with PII replaced by tokens."""
    tokenized_text = tokenize_text(request.text, _analyzer, _vault)
    return TokenizeResponse(tokenized_text=tokenized_text)


@app.post("/detokenize", response_model=DetokenizeResponse)
def detokenize(
    request: DetokenizeRequest,
    x_internal_vault_key: Optional[str] = Header(None, alias="X-Internal-Vault-Key"),
) -> DetokenizeResponse:
    """
    The 'Reveal Identity' endpoint. Given a token, returns the real value.
    Restricted to internal backend services with a valid internal key to prevent
    unauthorized PII exfiltration.
    """
    if not x_internal_vault_key or x_internal_vault_key != INTERNAL_VAULT_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Direct access to vault detokenization is restricted to backend services only.",
        )

    real_value = _vault.get_real_value(request.token)
    if real_value is None:
        raise HTTPException(status_code=404, detail=f"Token '{request.token}' not found in vault")

    return DetokenizeResponse(
        token=request.token,
        real_value=real_value,
        on_watchlist=_vault.is_on_watchlist(request.token),
    )


@app.get("/health")
def health():
    """Simple endpoint so teammates/infra can check the service is up."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    # Default to port 8002 to avoid conflict with backend (8000) and pattern agent (8001)
    uvicorn.run("api:app", host="127.0.0.1", port=8002, reload=True)
