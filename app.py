import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("pipe.pkl", "rb"))

st.set_page_config(page_title="Food Delivery Time Prediction")

st.title("🚚 Food Delivery Time Prediction")

# User Inputs
order_id = st.number_input("Order ID", min_value=1, step=1)
distance = st.number_input("Distance (km)", min_value=0.0, format="%.2f")
weather = st.selectbox("Weather", ["Clear", "Cloudy", "Rainy", "Foggy"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])
prep_time = st.number_input("Preparation Time (min)", min_value=0)
experience = st.number_input("Courier Experience (years)", min_value=0.0, format="%.1f")

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

    try:
        prediction = model.predict(features)
        st.success(f"Estimated Delivery Time: {round(prediction[0],2)} minutes")
    except Exception as e:
        st.error(e)