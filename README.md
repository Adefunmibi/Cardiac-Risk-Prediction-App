
# 🫀 Cardiac Risk Prediction App

A Streamlit-powered web application that predicts the likelihood of heart disease based on user inputs such as blood pressure, ECG results, and other clinical parameter.
Built to support early detection and promote awareness of cardiovascular health.

---

## 📋 Project Overview

This project is a web-based **Cardiac Risk Prediction App** built with Streamlit. 
It leverages machine learning to assess the likelihood of heart disease based on user-provided health metrics such as blood pressure, ECG results, cholesterol levels, and more.. 
The app is designed to be intuitive, educational, and engaging—with dropdowns for encoded categories, visual feedback using Lottie animations, and personalized health tips.
Whether you're a data scientist, healthcare enthusiast, or someone curious about your heart health, this app offers a hands-on way to explore predictive modeling in medicine.

---

## 🧠 Problem Statement
Cardiovascular diseases (CVDs) remain the leading cause of death globally, often due to late diagnosis and limited access to early screening tools. 
Many individuals are unaware of their risk levels until symptoms become severe. There is a pressing need for accessible, data-driven tools that can help predict cardiac risk 
using basic clinical inputs—empowering users and healthcare providers to take proactive steps.

---

## 🚀 Features

- 🧾 Interactive form for entering medical data
- 🔍 Encoded categories mapped to human-readable labels
- 🧠 Real-time prediction using a trained machine learning model
- 🎬 Visual feedback with Lottie animations and color-coded alerts
- 💡 Health tips based on user input
- 📈 Optional charts for trend visualization
- 🎨 Clean, responsive UI built with Streamlit

---

## 🧪 Technologies Used

- Python 🐍
- Streamlit
- scikit-learn
- pandas
- streamlit-lottie
- Matplotlib / Plotly (optional for charts)

 ### 🧰 Tech Stack

| Layer            | Tools & Libraries                          |
|------------------|--------------------------------------------|
| Frontend         | Streamlit, streamlit-lottie                |
| Backend          | Python, pandas, scikit-learn               |
| Visualization    | Matplotlib, Plotly (optional)              |
| Model Training   | XGB-Boost / Random Forest        |
| Deployment       | Localhost / Streamlit Cloud                |

---
## 📈 Model Performance

The model was trained using XGBOOST.

| Metric         | Score     |
|----------------|-----------|
| Accuracy       | 76%       |
| Precision      | 73%       |
| Recall         | 82%       |
| F1 Score       | 77%       |
| ROC-AUC        | 0.82      |

## 📊 Input Parameters

| Feature            | Description                                      |
|--------------------|--------------------------------------------------|
| Age                | Patient's age                                    |
| Sex                | 0 = Female, 1 = Male                             |
| Chest Pain Type    | 0–3 (e.g., typical angina, asymptomatic, etc.)   |
| Resting BP         | Systolic blood pressure (mmHg)                   |
| Cholesterol        | Serum cholesterol (mg/dl)                        |
| Fasting Sugar      | >120 mg/dl (1 = True, 0 = False)                 |
| Resting ECG        | 0 = Normal, 1 = ST-T abnormality, 2 = LVH        |
| Max Heart Rate     | Achieved during exercise                         |
| Exercise Angina    | 0 = No, 1 = Yes                                  |
| ST Slope           | 0 = Upsloping, 1 = Flat, 2 = Downsloping         |
| Major Vessels (ca) | 0–3 colored by fluoroscopy                       |
| Thalassemia        | 0–3 (e.g., normal, fixed defect, reversible)     |

---

## 🧠 How It Works

1. User enters clinical data via dropdowns and number inputs.
2. Data is preprocessed and fed into a trained ML model.
3. The model outputs a binary prediction: **Risk** or **No Risk**.
4. The app displays feedback with animations, and tips.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/cardiac-risk-app.git
cd cardiac-risk-app
pip install -r requirements.txt
streamlit run app.py
