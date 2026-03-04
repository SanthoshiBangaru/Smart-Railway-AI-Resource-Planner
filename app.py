import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_generator import generate_synthetic_data
from model import train_model
from optimizer import allocate_platform, congestion_score

st.set_page_config(page_title="SmartRail Planner", layout="wide")

st.title("🚆 SmartRail AI Resource Planner")

data = generate_synthetic_data(1000)

model, mae = train_model(data)

st.sidebar.header("Simulation Controls")

selected_station = st.sidebar.selectbox(
    "Select Station",
    data["station"].unique()
)

filtered_data = data[data["station"] == selected_station]

st.subheader("📊 Dataset Overview")
st.dataframe(filtered_data.head())

st.subheader("📈 Delay Distribution")

plt.figure()
plt.hist(filtered_data["delay_minutes"], bins=20)
st.pyplot(plt)

st.subheader("🤖 Model Performance")
st.write(f"Mean Absolute Error: {round(mae,2)} minutes")

st.subheader("🏗 Platform Allocation")
platforms = allocate_platform(filtered_data)
st.write(platforms)

st.subheader("🚦 Congestion Score")
score = congestion_score(filtered_data)
st.write(f"Congestion Score: {score}")

st.success("System Analysis Completed Successfully")