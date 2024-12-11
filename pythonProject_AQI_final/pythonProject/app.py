import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import joblib

# Load the trained model and scaler
model = joblib.load('AQI_Prediction_DL.pkl')
scaler = joblib.load(r'scaler.pkl')  # Save the scaler using joblib

# Title
st.title("Air Quality Index (AQI) Prediction App")

# Description
st.markdown("""
This app predicts the *Air Quality Index (AQI)* based on air pollutant levels. 
Please enter the values for the features below and click *Predict*.
""")

# Sidebar for user input
st.sidebar.header("Input Features")


def user_input_features():
    PM25 = st.sidebar.number_input('PM2.5', min_value=0.0, value=14.41)
    PM10 = st.sidebar.number_input('PM10', min_value=0.0, value=66.81)
    NO = st.sidebar.number_input('NO', min_value=0.0, value=6.22)
    NO2 = st.sidebar.number_input('NO2', min_value=0.0, value=40.06)
    NOx = st.sidebar.number_input('NOx', min_value=0.0, value=26.1)
    NH3 = st.sidebar.number_input('NH3', min_value=0.0, value=7.51)
    CO = st.sidebar.number_input('CO', min_value=0.0, value=1.07)
    SO2 = st.sidebar.number_input('SO2', min_value=0.0, value=13.23)
    O3 = st.sidebar.number_input('O3', min_value=0.0, value=27.34)
    Benzene = st.sidebar.number_input('Benzene', min_value=0.0, value=2.55)
    Toluene = st.sidebar.number_input('Toluene', min_value=0.0, value=8.98)
    Xylene = st.sidebar.number_input('Xylene', min_value=0.0, value=1.45)

    data = {
        'PM2.5': PM25,
        'PM10': PM10,
        'NO': NO,
        'NO2': NO2,
        'NOx': NOx,
        'NH3': NH3,
        'CO': CO,
        'SO2': SO2,
        'O3': O3,
        'Benzene': Benzene,
        'Toluene': Toluene,
        'Xylene': Xylene
    }
    features = pd.DataFrame(data, index=[0])
    return features


# Load user input
input_df = user_input_features()

# Main panel
st.subheader("User Input Parameters")
st.write(input_df)

# Predict AQI
if st.button('Predict'):
    # Scale input data
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0][0]

    # Classification
    if prediction <= 50:
        category = "Good"
    elif prediction <= 100:
        category = "Moderate"
    elif prediction <= 200:
        category = "Poor"
    elif prediction <= 300:
        category = "Unhealthy"
    elif prediction <= 400:
        category = "Severe"
    else:
        category = "Hazardous"

    # Display results
    st.subheader("Predicted AQI")
    st.write(f"{prediction:.2f}")
    st.subheader("Air Quality Category")
    st.write(category)