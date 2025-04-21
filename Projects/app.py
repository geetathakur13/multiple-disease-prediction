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
    'diabetes': pickle.load(open('Projects/Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Projects/Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Projects/Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Projects/Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Projects/Models/Thyroid_model.sav', 'rb'))
}

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

# CHATBOT SECTION
st.markdown("---")
st.subheader("💬 Health Assistant Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything about diseases, symptoms, or models...", key="chat_input")

if user_input:
    response = f"You asked: '{user_input}'. I'm here to help you with your health queries! 🩺"
    
    # Append to history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))
    
    # Reset the text input field after receiving input
    st.text_input("Ask me anything about diseases, symptoms, or models...", value="", key="chat_input")

# Display chat history
for sender, msg in st.session_state.chat_history:
    message(msg, is_user=(sender == "user"))

# CSS for white text
st.markdown("""
   <style>
   .reportview-container .main .block-container {
       color: white;
   }
   </style>
""", unsafe_allow_html=True)
