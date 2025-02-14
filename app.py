import streamlit as st
from streamlit_option_menu import option_menu
from kidney_disease import predict_kidney_disease
from heart_disease import predict_heart_disease
from diabetes import predict_diabetes
import pickle

# Load the models
kidney_disease_model = pickle.load(
    open('models/trained_model_kidney.pkl', 'rb'))
heart_disease_model = pickle.load(open('models/trained_model_heart.sav', 'rb'))
diabetes_model = pickle.load(open('models/trained_model_diabetes.sav', 'rb'))

st.set_page_config(page_title="Multiple Disease Prediction System",
                   page_icon="hospital", layout="wide")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Home Page',
                            'Heart Disease Prediction', 'Diabetes Prediction', 'Kidney Disease Prediction',],
                           menu_icon='hospital',
                           icons=['info', 'activity',
                                  'eyedropper', 'lungs-fill'],
                           default_index=0)

# General Instructions Page
if selected == 'Home Page':
    st.title('Welcome to Multiple Disease Prediction System!')
    st.write("Please select a disease prediction system from the sidebar.")
    st.image("images/MDPSImage.jpg")

# Disease Prediction Pages
elif selected == 'Kidney Disease Prediction':
    predict_kidney_disease(kidney_disease_model)
elif selected == 'Heart Disease Prediction':
    predict_heart_disease(heart_disease_model)
elif selected == 'Diabetes Prediction':
    predict_diabetes(diabetes_model)
