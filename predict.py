"""
Script untuk melakukan prediksi PUE dengan model yang sudah disimpan.
Script ini handle preprocessing data mentah secara otomatis.

Usage:
    python predict.py

Author: Your Name
Date: 2026-06-12
"""

import joblib
import pandas as pd
import glob
import os


def preprocess_and_predict(raw_data, model_dir='models', timestamp_version=None):
    """
    Function lengkap untuk prediksi dari data MENTAH.
    Melakukan preprocessing yang sama seperti saat training.
    
    Parameters:
    -----------
    raw_data : dict or DataFrame
        Data mentah dengan kolom original (seperti di CSV)
        Contoh: {
            'Year': 2023,
            'Facility_Type': 'Enterprise/Standard',
            'Estimated_Capacity_MW': 10.5,
            'Cooling_System_Type': 'Evaporative',
            'WUE_L_per_kWh': 1.2,
            'Daily_Electricity_Usage_MWh': 250.0,
            'Daily_Water_Usage_Gallons': 50000.0,
            'Surrounding_Water_Stress_Tier': 'Low'
        }
    model_dir : str
        Folder tempat model disimpan
    timestamp_version : str
        Timestamp version model (jika None, ambil yang terbaru)
        
    Returns:
    --------
    float : Prediksi nilai PUE
    """
    
    # Jika timestamp tidak diberikan, ambil file terbaru
    if timestamp_version is None:
        model_files = glob.glob(f'{model_dir}/best_model_*.joblib')
        if not model_files:
            raise FileNotFoundError(f"No model found in {model_dir}")
        latest_file = max(model_files, key=os.path.getctime)
        timestamp_version = latest_file.split('_')[-1].replace('.joblib', '')
    
    # Load semua preprocessing objects
    model = joblib.load(f'{model_dir}/best_model_{timestamp_version}.joblib')
    scaler = joblib.load(f'{model_dir}/scaler_{timestamp_version}.joblib')
    feature_names = joblib.load(f'{model_dir}/feature_names_{timestamp_version}.joblib')
    preprocessing_info = joblib.load(f'{model_dir}/preprocessing_info_{timestamp_version}.joblib')
    
    # Convert ke DataFrame jika dict
    if isinstance(raw_data, dict):
        df = pd.DataFrame([raw_data])
    else:
        df = raw_data.copy()
    
    # 1. Drop kolom yang tidak dipakai (kecuali PUE karena ini data baru)
    cols_to_drop = [col for col in preprocessing_info['drop_columns'] 
                    if col in df.columns and col != 'PUE']
    df = df.drop(columns=cols_to_drop, errors='ignore')
    
    # 2. Ordinal Encoding: Water Stress Tier
    if 'Surrounding_Water_Stress_Tier' in df.columns:
        df['Water_Stress_Encoded'] = df['Surrounding_Water_Stress_Tier'].map(
            preprocessing_info['water_stress_mapping']
        )
        df = df.drop(columns=['Surrounding_Water_Stress_Tier'])
    
    # 3. One-Hot Encoding: Categorical features
    df = pd.get_dummies(df, columns=preprocessing_info['categorical_features'], 
                        drop_first=False, dtype=int)
    
    # 4. Pastikan semua kolom ada (tambahkan kolom missing dengan nilai 0)
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0
    
    # 5. Reorder kolom sesuai urutan training
    df = df[feature_names]
    
    # 6. Scaling
    scale_cols = preprocessing_info['scale_columns']
    df[scale_cols] = scaler.transform(df[scale_cols])
    
    # 7. Prediksi
    prediction = model.predict(df)[0]
    
    return prediction


def main():
    """
    Contoh penggunaan function preprocess_and_predict
    """
    # Contoh data mentah
    sample_raw_data = {
        'Year': 2023,
        'Facility_ID': 'DC-TEST001',
        'Facility_Name': 'Test Facility',
        'Owner_Company': 'Test Corp',
        'City': 'Jakarta',
        'Country': 'Indonesia',
        'Facility_Type': 'Enterprise/Standard',
        'Estimated_Capacity_MW': 10.5,
        'Cooling_System_Type': 'Evaporative',
        'WUE_L_per_kWh': 1.2,
        'Daily_Electricity_Usage_MWh': 250.0,
        'Daily_Water_Usage_Gallons': 50000.0,
        'Surrounding_Water_Stress_Tier': 'Low'
    }
    
    print('🧪 Testing Prediction with Raw Data\n')
    print('📋 Input Data:')
    for key, value in sample_raw_data.items():
        print(f'   {key:35s}: {value}')
    
    try:
        # Prediksi
        predicted_pue = preprocess_and_predict(sample_raw_data)
        
        print(f'\n🎯 Predicted PUE: {predicted_pue:.4f}')
        print('\n✅ Prediction successful!')
        
        # Interpretasi hasil
        if predicted_pue < 1.5:
            efficiency = 'Sangat Efisien'
        elif predicted_pue < 1.8:
            efficiency = 'Efisien'
        elif predicted_pue < 2.0:
            efficiency = 'Cukup Efisien'
        else:
            efficiency = 'Perlu Optimasi'
            
        print(f'📊 Efficiency Level: {efficiency}')
        
    except Exception as e:
        print(f'\n❌ Error: {str(e)}')
        print('   Pastikan model sudah di-training dan disimpan di folder models/')


if __name__ == '__main__':
    main()
