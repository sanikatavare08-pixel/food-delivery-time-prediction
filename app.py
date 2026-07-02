import streamlit as st
import pickle
import numpy as np
import pandas as pd


# Load trained model
model = pickle.load(open("pipe.pkl", "rb"))

st.title("🚚 Food Delivery Time Prediction")

order_id = st.number_input("Order ID", min_value=1, step=1)
distance = st.number_input("Distance (km)", min_value=0.0)
weather = st.selectbox("Weather", ["Sunny", "Cloudy", "Rainy", "Foggy"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])
prep_time = st.number_input("Preparation Time (min)", min_value=0.0)
experience = st.number_input("Courier Experience (years)", min_value=0.0)

# Encode categorical values (replace with your actual encoding)
weather_map = {
    "Sunny": 0,
    "Cloudy": 1,
    "Rainy": 2,
    "Foggy": 3
}

traffic_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

time_map = {
    "Morning": 0,
    "Afternoon": 1,
    "Evening": 2,
    "Night": 3
}

vehicle_map = {
    "Bike": 0,
    "Scooter": 1,
    "Car": 2
}

if st.button("Predict Delivery Time"):
    features = pd.DataFrame({
    "Order_ID": [order_id],
    "Distance_km": [distance],
    "Weather": [weather],
    "Traffic_Level": [traffic],
    "Time_of_Day": [time_of_day],
    "Vehicle_Type": [vehicle],
    "Preparation_Time_min": [prep_time],
    "Courier_Experience_yrs": [experience]
})
    

    prediction = model.predict(features)

    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")
