import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("insurance_model.pkl")

st.image("c:/Users/Admin/Downloads/insurance.jpg", caption="My Image", use_container_width=True)


st.title("💼 Insurance Premium Prediction App")
st.write("Enter the customer details to estimate medical insurance premium")

# Input Fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=26.5)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Input DataFrame
input_data = pd.DataFrame({
    "age":[age], "sex":[sex], "bmi":[bmi],
    "children":[children], "smoker":[smoker], "region":[region]
})

# Predict Button
if st.button("Predict Insurance Premium"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Premium: 💰 **₹{prediction[0]:.2f}**")