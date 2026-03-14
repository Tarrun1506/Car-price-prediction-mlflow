import joblib
import pandas as pd
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / 'model.pkl'

def test_prediction():
    if not MODEL_PATH.exists():
        print(f"Model file not found at {MODEL_PATH}. Please run train_model.py first.")
        return

    model = joblib.load(MODEL_PATH)
    
    # Sample input matching the features in the training data
    sample_data = pd.DataFrame([{
        'name': 'Maruti Swift Dzire VDI',
        'year': 2014,
        'km_driven': 145500,
        'fuel': 'Diesel',
        'seller_type': 'Individual',
        'transmission': 'Manual',
        'owner': 'First Owner',
        'mileage(km/ltr/kg)': 23.40,
        'engine': 1248.0,
        'max_power': 74.0,
        'seats': 5.0
    }])
    
    prediction = model.predict(sample_data)[0]
    print(f"Sample Car Input:\n{sample_data.iloc[0]}")
    print(f"\nPredicted Selling Price: Rs. {prediction:,.2f}")

if __name__ == "__main__":
    test_prediction()
