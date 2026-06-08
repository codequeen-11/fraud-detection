# Fraud Detection Project

A machine learning repository focused on detecting fraud using generated datasets that replace the original challenge-sourced files.

> **Challenge note:** The original challenge datasets have been archived in `data/archive/`. The active datasets used by this project reside in `data/raw/`.

1. **Credit Card Fraud Detection** — dataset with business-inspired transaction risk features, transaction amount, and time.
2. **E-commerce Fraud Detection** — transaction data with signup/purchase behavior, device and IP metadata.

---

## Project Structure

```
fraud-detection/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── data/                           # Excluded from git
│   ├── raw/                        # Original datasets
│   └── processed/                  # Cleaned and feature-engineered data
├── notebooks/
│   ├── eda-creditcard.ipynb        # Credit card EDA
│   ├── eda-fraud-data.ipynb        # E-commerce EDA
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   └── shap-explainability.ipynb
├── src/
├── tests/
├── models/                         # Saved model artifacts
├── scripts/
│   └── generate_synthetic_fraud.py # Generate fraud datasets
├── requirements.txt
└── README.md
```
 
 


## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Download Raw Data

```bash
python3 scripts/download_data.py
```

### Running EDA Notebooks

```bash
jupyter notebook
```

