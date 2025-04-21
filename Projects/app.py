import streamlit as st
import pickle
import numpy as np
from chatbot import get_chatbot_response

# Load models
diabetes_model = pickle.load(open("models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("models/parkinsons_model.sav", "rb"))
lung_cancer_model = pickle.load(open("models/lung_cancer_model.sav", "rb"))
thyroid_model = pickle.load(open("models/thyroid_model.sav", "rb"))

# App layout
st.set_page_config(page_title="Disease Prediction with Chatbot", layout="wide")
st.markdown(
    "<style> .stApp { background-image: url('https://wallpaperaccess.com/full/4723256.jpg'); background-size: cover; } </style>",
    unsafe_allow_html=True,
)
st.markdown("<h1 style='text-align: center; color: white;'>Health Assistant Chatbot</h1>", unsafe_allow_html=True)

# Dropdown to select disease
disease = st.selectbox("Select a Disease to Predict", ["Diabetes", "Heart Disease", "Parkinsons", "Lung Cancer", "Hypo-Thyroid"])

# Prediction form
def user_input_features():
    if disease == "Diabetes":
        Pregnancies = st.number_input("Pregnancies")
        Glucose = st.number_input("Glucose")
        BloodPressure = st.number_input("BloodPressure")
        SkinThickness = st.number_input("SkinThickness")
        Insulin = st.number_input("Insulin")
        BMI = st.number_input("BMI")
        DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
        Age = st.number_input("Age")
        return [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    elif disease == "Heart Disease":
        age = st.number_input("Age")
        sex = st.number_input("Sex (1 = Male, 0 = Female)")
        cp = st.number_input("Chest Pain Type")
        trestbps = st.number_input("Resting Blood Pressure")
        chol = st.number_input("Cholesterol")
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)")
        restecg = st.number_input("Resting ECG results")
        thalach = st.number_input("Max heart rate achieved")
        exang = st.number_input("Exercise induced angina (1 = yes; 0 = no)")
        oldpeak = st.number_input("ST depression induced by exercise")
        slope = st.number_input("Slope of the peak exercise ST segment")
        ca = st.number_input("Number of major vessels (0-3) colored by fluoroscopy")
        thal = st.number_input("Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)")
        return [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    elif disease == "Parkinsons":
        fo = st.number_input("MDVP:Fo(Hz)")
        fhi = st.number_input("MDVP:Fhi(Hz)")
        flo = st.number_input("MDVP:Flo(Hz)")
        jitter_percent = st.number_input("MDVP:Jitter(%)")
        shimmer = st.number_input("MDVP:Shimmer")
        NHR = st.number_input("NHR")
        HNR = st.number_input("HNR")
        RPDE = st.number_input("RPDE")
        DFA = st.number_input("DFA")
        spread1 = st.number_input("spread1")
        spread2 = st.number_input("spread2")
        D2 = st.number_input("D2")
        PPE = st.number_input("PPE")
        return [fo, fhi, flo, jitter_percent, shimmer, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

    elif disease == "Lung Cancer":
        age = st.number_input("Age")
        smoking = st.number_input("Smoking (1 = Yes, 0 = No)")
        anxiety = st.number_input("Anxiety (1 = Yes, 0 = No)")
        peer_pressure = st.number_input("Peer Pressure")
        chronic_disease = st.number_input("Chronic Disease (1 = Yes, 0 = No)")
        fatigue = st.number_input("Fatigue")
        allergy = st.number_input("Allergy (1 = Yes, 0 = No)")
        wheezing = st.number_input("Wheezing (1 = Yes, 0 = No)")
        alcohol = st.number_input("Alcohol (1 = Yes, 0 = No)")
        coughing = st.number_input("Coughing (1 = Yes, 0 = No)")
        shortness_of_breath = st.number_input("Shortness of Breath (1 = Yes, 0 = No)")
        swallowing_difficulty = st.number_input("Swallowing Difficulty (1 = Yes, 0 = No)")
        chest_pain = st.number_input("Chest Pain (1 = Yes, 0 = No)")
        return [age, smoking, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]

    elif disease == "Hypo-Thyroid":
        age = st.number_input("Age")
        sex = st.number_input("Sex (0 = Female, 1 = Male)")
        on_thyroxine = st.number_input("On thyroxine (1 = Yes, 0 = No)")
        query_on_thyroxine = st.number_input("Query on thyroxine")
        on_antithyroid_medication = st.number_input("On antithyroid medication")
        sick = st.number_input("Sick")
        pregnant = st.number_input("Pregnant")
        thyroid_surgery = st.number_input("Thyroid surgery")
        I131_treatment = st.number_input("I131 treatment")
        TSH_measured = st.number_input("TSH measured")
        return [age, sex, on_thyroxine, query_on_thyroxine, on_antithyroid_medication, sick, pregnant, thyroid_surgery, I131_treatment, TSH_measured]

input_data = user_input_features()

# Predict button
if st.button("Predict"):
    input_array = np.asarray(input_data).reshape(1, -1)
    if disease == "Diabetes":
        result = diabetes_model.predict(input_array)
    elif disease == "Heart Disease":
        result = heart_disease_model.predict(input_array)
    elif disease == "Parkinsons":
        result = parkinsons_model.predict(input_array)
    elif disease == "Lung Cancer":
        result = lung_cancer_model.predict(input_array)
    elif disease == "Hypo-Thyroid":
        result = thyroid_model.predict(input_array)

    st.success(f"Prediction: {'Positive' if result[0] == 1 else 'Negative'}")

# Chatbot section
st.markdown("### Assistant Chatbot 🧠💬")
user_input = st.text_input("Ask me anything about diseases or models...")
if user_input:
    response = get_chatbot_response(user_input)
    st.write(response)

if st.button("Clear Chat History"):
    st.experimental_rerun()
