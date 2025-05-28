import streamlit as st 
import pickle
import pandas as pd
import numpy as np


with open('classification_model.pkl','rb') as f:
    model=pickle.load(f)
    
with open('scaler.pkl','rb') as f:
    scaler = pickle.load(f)   
    
    
st.title('Income Prediction App')

age=st.number_input('age')    
education_num=st.number_input('education-num')
capital_gain=st.number_input('capital-gain')
capital_loss=st.number_input('capital-loss')
hours_per_week=st.number_input('hours-per-week')
marital_status_Married_civ_spouse = st.radio("Are you Married (civil spouse)?", ["Yes", "No"])
occupation_Sales = st.radio("Occupation is Sales?", ["Yes", "No"])

# Encoding binary categorical features
marital_status_Married_civ_spouse = 1 if marital_status_Married_civ_spouse == "Yes" else 0
occupation_Sales = 1 if occupation_Sales == "Yes" else 0


input_df=pd.DataFrame([{
    'age': age,
    'education-num': education_num,
    'capital-gain': capital_gain,
    'capital-loss': capital_loss,
    'hours-per-week': hours_per_week,
    'marital-status_Married-civ-spouse': marital_status_Married_civ_spouse,
    'occupation_Sales': occupation_Sales
}])
num_cols_to_standardize = ['age', 'capital-gain', 'capital-loss', 'hours-per-week']
input_df[num_cols_to_standardize] = scaler.transform(input_df[num_cols_to_standardize])
input_df['age'] = np.log1p(input_df['age'])


if st.button("Predict Income"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success("Predicted income is above 50k ")
    else:
        st.info("Predicted income is below 50k ")
    