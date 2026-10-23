# IBM Team TechyByte — Privacy-Preserving Risk Analysis

A privacy-focused data analysis project that combines tokenization, entity linkage, pattern detection, graph-based analysis, and behavioral anomaly detection to support explainable risk assessment.

## Overview

Financial and employee-related datasets may contain personally identifiable information (PII), making it important to protect sensitive data while still identifying potentially suspicious patterns.

**IBM Team TechyByte** explores a modular approach to privacy-preserving data processing and risk analysis. The project tokenizes sensitive identifiers and combines analytical signals from different agents to produce a consolidated risk assessment with supporting evidence.

The project is developed as a team effort, with individual components contributing to the overall workflow.

## Key Features

- **Privacy-Preserving Tokenization:** Replaces sensitive identifiers with tokens to reduce direct exposure of personal information during analysis.
- **Token Vault:** Maintains token-to-identity mappings and supports controlled identity lookup.
- **Watchlist Linkage:** Represents watchlist status using token-linked data.
- **Pattern Detection:** Analyzes transaction information for potentially suspicious patterns.
- **Graph-Based Analysis:** Examines relationships between entities to identify linked activities.
- **Behavioral Anomaly Detection:** Uses machine learning to identify unusual behavioral patterns.
- **Risk Aggregation:** Combines signals from multiple analytical components into a consolidated risk score and risk level.
- **Explainable Results:** Presents supporting signals, evidence, and recommended follow-up actions to assist human review.

## System Architecture

The project follows a modular, multi-agent workflow:

1. **Data Input:** Transaction or employee-related records are provided for analysis.
2. **Tokenization Layer:** Sensitive identifiers are converted into tokens.
3. **Analytical Agents:** Pattern detection, graph analysis, and KYC/behavioral checks generate individual findings.
4. **Aggregator:** Combines the available results and calculates a heuristic risk score.
5. **Explainability Layer:** Returns the risk level, supporting evidence, signals, and suggested next steps.

```text
Input Data
    |
    v
Privacy-Preserving Tokenization
    |
    v
Analytical Agents
    |
    +--> Pattern Detection
    |
    +--> Graph Analysis
    |
    +--> KYC and Behavioral Analysis
    |
    v
Risk Aggregator
    |
    v
Risk Score + Evidence + Recommended Action
    |
    v
Human Review
```

## Risk Aggregation and Explainability

The aggregator consolidates outputs from the pattern, graph, KYC, and behavioral components.

The current demo scoring logic assigns:

| Signal | Points |
|---|---:|
| Pattern flag | 30 |
| KYC match | 30 |
| Behavioral anomaly | 30 |
| Non-zero linked graph ring size | 10 |

The resulting score is interpreted using these thresholds:

| Score | Risk Level |
|---|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–100 | HIGH |

The output includes the risk score, risk level, detected signals, evidence, a recommended next action, and whether human review is required.

**Important:** This is a demonstration heuristic, not a validated fraud probability or a production-ready risk model. The score depends on the outputs and quality of the underlying agents.

## Technology Stack

- **Python** — Core implementation and orchestration
- **Pandas** — Data handling and preprocessing
- **Scikit-learn** — Machine-learning-based anomaly detection
- **RapidFuzz** — Fuzzy matching for KYC checks
- **Pytest** — Automated testing
- **GitHub Actions** — Automated test workflows
- **JSON and CSV** — Structured data and token-linkage artifacts

## Repository Contents

The repository contains the project's implementation, data artifacts, tests, and automation workflows.

| File or component | Purpose |
|---|---|
| `aggregator.py` | Consolidates agent results and calculates risk scores |
| `test_aggregator.py` | Unit tests for the aggregator |
| `integration_test.py` | Integration test script |
| `test.yml` | Automated test workflow |
| `integration.yml` | Integration workflow |
| `tokenizer.py` | Tokenization-related implementation |
| `structured_tokenizer.py` | Structured-data tokenization |
| `vault.py` | Token vault functionality |
| `token_watchlist_linkage.json` | Token-to-watchlist-status mapping |
| `tokenized_dataset.json` | Tokenized transaction data |
| `tokenized_employee_dataset.csv` | Tokenized employee dataset |
| `raw_transactions.csv` | Transaction input data |
| `requirements.txt` | Python dependency list |

Additional agent modules and analysis artifacts are included in the repository.

## Getting Started

### Prerequisites

- Python 3.10 or a compatible Python version
- Git
- pip

### Installation

Clone the repository:

```bash
git clone https://github.com/anshul-agarwal3034/IBM_Team_TechyByte.git
cd IBM_Team_TechyByte
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the listed dependencies:

```bash
pip install -r requirements.txt
```

### Running Tests

If the aggregator files are located in the repository root, run:

```bash
pytest -v test_aggregator.py
```

If the aggregator files are inside an `aggregator/` directory, run:

```bash
pytest -v aggregator/test_aggregator.py
```

The integration test may require the relevant agent modules, their dependencies, datasets, and any required services to be available. Follow the corresponding module configuration before running the complete integration workflow.

## Testing and Continuous Integration

The repository includes GitHub Actions workflow files intended to automate testing and integration checks.

Test results depend on the repository's file structure, dependency configuration, and workflow setup. A successful file upload alone does not establish that every workflow passes.

## Privacy and Responsible Use

- Avoid exposing raw personal information in public repositories.
- Do not commit credentials, private keys, or sensitive identity mappings.
- Use synthetic or appropriately anonymized data for public demonstrations.
- Restrict access to token-vault mappings and detokenization functionality.
- Treat automated risk assessments as decision-support signals rather than definitive conclusions.
- Require human review before taking consequential action based on risk outputs.

## Limitations

This project is a prototype intended for experimentation and demonstration. Its results depend on the available data, tokenization quality, watchlist configuration, model behavior, and integration between agents.

The scoring logic has not been established as a calibrated probability of fraud, and the system should not be treated as a substitute for validated investigation procedures.

## Team

**Project:** IBM Team TechyByte  
**Repository:** [IBM_Team_TechyByte](https://github.com/anshul-agarwal3034/IBM_Team_TechyByte)

Developed collaboratively as a modular privacy-preserving data analysis and risk assessment project.

---

*Built to explore how privacy-conscious data processing, machine learning, and explainable risk analysis can work together.*
