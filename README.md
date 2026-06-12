# 🏭 Data Center PUE Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Proyek Machine Learning untuk memprediksi **PUE (Power Usage Effectiveness)** pada fasilitas Data Center menggunakan berbagai algoritma ML.

## 📋 Deskripsi Project

PUE (Power Usage Effectiveness) adalah metrik efisiensi energi pada data center. Semakin mendekati 1.0, semakin efisien data center tersebut. Project ini membangun model prediktif untuk membantu operator data center mengoptimalkan konsumsi energi.

## 🎯 Fitur Utama

- ✅ **Exploratory Data Analysis (EDA)** lengkap dengan visualisasi
- ✅ **Data Preprocessing** termasuk encoding, scaling, dan train-test split
- ✅ **Multiple ML Models**: Linear Regression, Random Forest, Gradient Boosting
- ✅ **Model Evaluation** dengan MAE, RMSE, dan R² Score
- ✅ **Feature Importance Analysis**
- ✅ **Model Deployment** dengan preprocessing pipeline lengkap
- ✅ **Production-ready Prediction Function**

## 📊 Dataset
- Kaggle: [Global Data Center & AI Water/Electricity Usage](https://www.kaggle.com/datasets/ashyou09/global-data-center-and-ai-waterelectricity-usage)
- Dataset berisi **126,770 data point** dengan **14 kolom**:

**Fitur Input:**
- Year
- Facility_Type (Enterprise/Standard, Hyperscale, Colocation)
- Estimated_Capacity_MW
- Cooling_System_Type (Evaporative, Air-Cooled, Water-Cooled, Liquid-Cooled)
- WUE_L_per_kWh
- Daily_Electricity_Usage_MWh
- Daily_Water_Usage_Gallons
- Surrounding_Water_Stress_Tier (Low, Med, High)

**Target:**
- PUE (Power Usage Effectiveness)

## 🚀 Quick Start

### Prerequisites

```bash
python >= 3.12
```

### Installation

1. Clone repository:
```bash
git clone https://github.com/YOUR_USERNAME/AiDataCenter.git
cd AiDataCenter
```

2. Buat virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# atau
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Notebook

```bash
jupyter notebook main.ipynb
```

## 📈 Hasil Model

| Model | Test MAE | Test RMSE | Test R² |
|-------|----------|-----------|---------|
| Linear Regression | 0.1253 | 0.1490 | 0.3889 |
| **Random Forest** ⭐ | **0.0674** | **0.0840** | **0.8057** |
| Gradient Boosting | 0.0822 | 0.0994 | 0.7278 |

🏆 **Model Terbaik**: Random Forest dengan R² = 0.8057

## 🔧 Cara Menggunakan Model untuk Prediksi

### 1. Load Model

```python
import joblib

# Load model dan preprocessing objects
model = joblib.load('models/best_model_XXXXXXXX.joblib')
scaler = joblib.load('models/scaler_XXXXXXXX.joblib')
preprocessing_info = joblib.load('models/preprocessing_info_XXXXXXXX.joblib')
```

### 2. Prediksi dengan Data Mentah

```python
from predict import preprocess_and_predict

# Contoh data mentah
raw_data = {
    'Year': 2023,
    'Facility_Type': 'Enterprise/Standard',
    'Estimated_Capacity_MW': 10.5,
    'Cooling_System_Type': 'Evaporative',
    'WUE_L_per_kWh': 1.2,
    'Daily_Electricity_Usage_MWh': 250.0,
    'Daily_Water_Usage_Gallons': 50000.0,
    'Surrounding_Water_Stress_Tier': 'Low'
}

# Prediksi
predicted_pue = preprocess_and_predict(raw_data)
print(f'Predicted PUE: {predicted_pue:.4f}')
```

## 📁 Struktur Project

```
AiDataCenter/
├── data_center_hybrid.csv      # Dataset
├── main.ipynb                   # Notebook utama
├── requirements.txt             # Python dependencies
├── models/                      # Folder untuk saved models
│   ├── best_model_*.joblib
│   ├── scaler_*.joblib
│   ├── feature_names_*.joblib
│   └── preprocessing_info_*.joblib
├── .gitignore                   # Git ignore file
└── README.md                    # Dokumentasi
```

## 🛠️ Tech Stack

- **Python 3.12**
- **pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine Learning
- **Matplotlib & Seaborn** - Visualization
- **Joblib** - Model serialization

## ⚠️ Catatan Penting

### Data Preprocessing

**Data baru HARUS melalui preprocessing yang sama seperti saat training:**

1. Drop kolom yang tidak dipakai (Facility_ID, Facility_Name, dll)
2. Ordinal Encoding untuk Water_Stress_Tier
3. One-Hot Encoding untuk Facility_Type dan Cooling_System_Type
4. StandardScaler untuk fitur numerik

### Model Versioning

Semua model disimpan dengan timestamp untuk versioning:
- `best_model_20260612_123456.joblib`
- `scaler_20260612_123456.joblib`
- dll.

## 📝 To-Do / Future Improvements

- [ ] Hyperparameter tuning dengan GridSearchCV
- [ ] Coba algoritma XGBoost dan LightGBM
- [ ] Deploy model sebagai REST API (Flask/FastAPI)
- [ ] Tambah unit tests
- [ ] CI/CD pipeline
- [ ] Docker containerization
- [ ] Interactive dashboard (Streamlit/Dash)

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**About Me!**
- GitHub: [@limm.](https://github.com/halimamrin312)
- LinkedIn: [limmm.](www.linkedin.com/in/halim-amrin)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

**Note**: Pastikan untuk tidak commit file model yang besar ke GitHub. Gunakan Git LFS atau simpan di cloud storage.
