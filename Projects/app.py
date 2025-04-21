from streamlit_chat import message
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hide Streamlit add-ons
hide_st_style = """
         <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Background Image
background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({background_image_url});
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load Models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}
# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Disease Prediction",
        options=["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction", "Lung Cancer Prediction", "Hypo-Thyroid Prediction"],
        icons=["activity", "heart", "person", "lungs", "medkit"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#f0f2f5"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#007bff"},
        }
    )
# Dropdown for Disease Selection
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Hypo-Thyroid Prediction']
)

# Common Input Function
def display_input(label, key, tooltip, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# PREDICTION PAGES (unchanged, already added above)...

# CHATBOT SECTION
st.markdown("---")
st.subheader("💬 Health Assistant Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything about diseases, symptoms, or models...", key="chat_input")
if user_input:
    # Here you can plug in any logic or ML model
    response = f"You asked: '{user_input}'. I'm here to help you with your health queries! 🩺"
    
    # Append to history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Display chat history
for sender, msg in st.session_state.chat_history:
    message(msg, is_user=(sender == "user"))

# Add a button to clear chat history
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.experimental_rerun()  # Refresh the app to clear the chat history
