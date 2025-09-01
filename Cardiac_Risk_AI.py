#Import the necessary libraries
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
from streamlit_lottie import st_lottie
import json

def load_animation(path):
    with open(path, "r") as f:
        return json.load(f)

heartbeat_animation = load_animation("heartbeat.json")

# 🎯 Page setup
st.set_page_config(page_title="Cardiac Risk Predictor 💓", page_icon="🫀", layout="centered")
st.title("🩺 Cardiac Disease Risk Prediction")
st.markdown("Let's check your heart health with a sprinkle of tech magic 🤖✨")
st_lottie(heartbeat_animation, height=250, loop=True)


#Import model
model=pickle.load(open("model_xgb.pkl","rb"))

# 🧾 Collect user inputs
age = st.number_input("🎂 Age (years)", min_value=1, max_value=120)
sex = st.selectbox("🚻 Sex", options=[0, 1], help="0 = Female, 1 = Male")
cp = st.selectbox("💔 Chest Pain Type", options=[0, 1, 2, 3],help="0=Typical,1=Atypical,2=Non-anginal,3=Asymptomatic")
trestbps = st.number_input("💥 Resting Blood Pressure (mm Hg)", min_value=80, max_value=200)
chol = st.number_input("🧪 Serum Cholesterol (mg/dL)", min_value=100, max_value=400)
fbs = st.selectbox("🧃 Fasting Blood Sugar > 120 mg/dL", options=[0, 1],help="0=False,1=True")
restecg = st.selectbox("📉 Resting ECG Results", options=[0, 1, 2],help="0=Normal,1=ST-T wave abnormality,2=Left ventricular hypertrophy")
thalach = st.number_input("🏃‍♂️ Max Heart Rate Achieved", min_value=60, max_value=220)
exang = st.selectbox("😰 Exercise-Induced Angina", options=[0, 1],help="0=No,1=Yes")
oldpeak = st.number_input("📉 ST Depression (Oldpeak)", min_value=0.0, max_value=6.0, step=0.1)
slope = st.selectbox("📈 Slope of Peak Exercise ST Segment", options=[0, 1, 2],help="0=Upsloping,1=Flat,2=Downsloping")
ca = st.selectbox("🩻 Major Vessels Colored by Fluoroscopy", options=[0, 1, 2, 3],help="0=0 vessels,1=1 vessel,2=2 vessels,3=3 vessels")
thal = st.selectbox("🧬 Thalassemia Status", options=[3, 6, 7],help=" 3 = normal, 6 = fixed defect, 7 = reversible defect")
smoking = st.selectbox("🚬 Smoking Status", options=[0, 1],help="0=No,1=Yes")
diabetes = st.selectbox("🍬 Diabetes Status", options=[0, 1],help="0=No,1=Yes")
bmi = st.number_input("⚖️ Body Mass Index (kg/m²)", min_value=10.0, max_value=60.0, step=0.1)


# 🧮 Prepare input for prediction
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                        exang, oldpeak, slope, ca, thal, smoking, diabetes, bmi]])


    
    # 🔍 Predict button
if st.button("🔎 Predict Risk"):
    prediction = model.predict(input_data)
    result = "🚨 High Risk of Cardiac Disease" if prediction[0] == 1 else "✅ Low Risk of Cardiac Disease"
    st.success(f"Prediction Result: {result}")
    st.balloons() if prediction[0] == 0 else st.warning("Please consult a doctor for further evaluation 🏥")
    

    # 🧠 Footer
st.markdown("---")
st.header("💡 Heart Health Tips")
st.markdown("""
- 🥗 Eat a balanced diet rich in fruits and vegetables  
- 🚶‍♀️ Stay active—aim for 30 minutes of movement daily  
- 🚭 Avoid smoking and limit alcohol  
- 🧘‍♂️ Manage stress with mindfulness or relaxation techniques  
""")
st.caption("Powered by XGBoost & Streamlit • Made with ❤️ by Adeola")
