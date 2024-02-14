import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk


model = pk.load(open('mera file .pkl' , 'rb'))

data=pd.read_csv('heart_disease.csv')

st.header( ' HEART DISEASE PREDICTOR ')

gender = st.selectbox( 'Choose Gender ',data['Gender'].unique() )

if gender == 'Male':
    gen=1
else:
    gen =0

age = st.number_input("Enter Age ")    
currentSmoker = st.number_input("Does patient currently smoke ") 
cigsPerDay = st.number_input(" Enter cigrattes consume per day by the person ") 
BPMeds= st.number_input("Does person is on Blood Pressure medication  ") 
prevalentStroke = st.number_input("Does the person ever suffered stroke") 
prevalentHyp = st.number_input("Ever suffered hyp ") 
diabetes = st.number_input("Does patient have Diabetics ") 
totChol = st.number_input("Is totChol") 
sysBP = st.number_input("Value of sys BP ") 
diaBP = st.number_input("Value of dia BP ") 
BMI = st.number_input("Enter Body Mass Index (BMI) ") 
heartRate = st.number_input("Enter Heart rate ") 
glucose = st.number_input("Glucose level  ") 


if st.button('Predict'):
    input=np.array([[gen,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI, heartRate,glucose]])
    output=model.predict(input)
    if output[0]==0:
        stn = ' Patient is healthy . No heart Disease '
    else :
        stn = ' Patient MAY have a Heart disease'
    st.markdown(stn)        


