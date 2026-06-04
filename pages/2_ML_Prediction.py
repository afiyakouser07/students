import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.ml_model import train_model

df = load_data()

st.title("🤖 Placement Prediction")

model, accuracy, features = train_model(df)

st.success(
    f"Model Accuracy : {accuracy*100:.2f}%"
)

st.subheader("Enter Student Details")

inputs = {}

for feature in features:

    inputs[feature] = st.number_input(
        feature,
        value=float(df[feature].mean())
    )

if st.button("Predict Placement"):

    input_df = pd.DataFrame([inputs])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("Placed")
    else:
        st.error("Not Placed")
