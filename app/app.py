import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'models' / 'model.pkl'
FALLBACK_MODEL_PATH = BASE_DIR / 'artifacts' / 'car_price_model.joblib'

st.set_page_config(page_title='Car Price Predictor', layout='wide')


@st.cache_resource
def load_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    if FALLBACK_MODEL_PATH.exists():
        return joblib.load(FALLBACK_MODEL_PATH)
    raise FileNotFoundError('Model file not found. Run the notebook first.')


model = load_model()

st.title('Car Price Prediction')
st.write('Enter the car details below to predict the selling price.')

with st.form('prediction_form'):
    left, right = st.columns(2)

    with left:
        name = st.text_input('Car name', value='')
        year = st.number_input('Year', min_value=1990, max_value=2030, value=None, step=1, placeholder='Enter year')
        km_driven = st.number_input(
            'Kilometers driven',
            min_value=0.0,
            value=None,
            step=1000.0,
            placeholder='Enter kilometers driven'
        )
        fuel = st.selectbox('Fuel type', ['Select fuel type', 'Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
        seller_type = st.selectbox(
            'Seller type',
            ['Select seller type', 'Individual', 'Dealer', 'Trustmark Dealer']
        )

    with right:
        transmission = st.selectbox('Transmission', ['Select transmission', 'Manual', 'Automatic'])
        owner = st.selectbox(
            'Owner history',
            ['Select owner history', 'First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car']
        )
        mileage = st.number_input(
            'Mileage (km/ltr/kg)',
            min_value=0.0,
            value=None,
            step=0.1,
            placeholder='Enter mileage'
        )
        engine = st.number_input(
            'Engine (CC)',
            min_value=0.0,
            value=None,
            step=50.0,
            placeholder='Enter engine capacity'
        )
        max_power = st.number_input(
            'Max power',
            min_value=0.0,
            value=None,
            step=1.0,
            placeholder='Enter max power'
        )
        seats = st.number_input(
            'Seats',
            min_value=1.0,
            max_value=10.0,
            value=None,
            step=1.0,
            placeholder='Enter number of seats'
        )

    submitted = st.form_submit_button('Predict Selling Price')

if submitted:
    if not name.strip():
        st.error('Enter the car name.')
    elif fuel == 'Select fuel type':
        st.error('Select a fuel type.')
    elif seller_type == 'Select seller type':
        st.error('Select a seller type.')
    elif transmission == 'Select transmission':
        st.error('Select a transmission type.')
    elif owner == 'Select owner history':
        st.error('Select owner history.')
    elif None in [year, km_driven, mileage, engine, max_power, seats]:
        st.error('Fill in all numeric fields.')
    else:
        input_df = pd.DataFrame([
            {
                'name': name.strip(),
                'year': int(year),
                'km_driven': float(km_driven),
                'fuel': fuel,
                'seller_type': seller_type,
                'transmission': transmission,
                'owner': owner,
                'mileage(km/ltr/kg)': float(mileage),
                'engine': float(engine),
                'max_power': float(max_power),
                'seats': float(seats),
            }
        ])
        prediction = float(model.predict(input_df)[0])
        st.success(f'Estimated selling price: Rs. {prediction:,.2f}')
