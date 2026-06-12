# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-06-12

### Added
- Initial release
- Exploratory Data Analysis (EDA) complete
- Data preprocessing pipeline
- Three ML models: Linear Regression, Random Forest, Gradient Boosting
- Model evaluation with MAE, RMSE, R² metrics
- Feature importance analysis
- Model deployment with joblib
- Production-ready prediction function
- Complete preprocessing pipeline for raw data

### Features
- **Dataset**: 126,770 data points dengan 14 kolom
- **Best Model**: Random Forest dengan R² = 0.8057
- **Preprocessing**: Ordinal encoding, One-Hot encoding, StandardScaler
- **Deployment Ready**: Script Python untuk prediksi (`predict.py`)

### Documentation
- README.md dengan quick start guide
- Code comments dalam notebook
- Docstrings untuk semua functions

## [Unreleased]

### Planned
- Hyperparameter tuning
- XGBoost dan LightGBM models
- REST API dengan Flask/FastAPI
- Interactive dashboard
- Unit tests
- CI/CD pipeline
- Docker containerization

---

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
