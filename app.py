import streamlit as st
import pandas as pd
import numpy as np
import pickle


with open("./pklFiles/model","rb") as file:
    BestModel=pickle.load(file)

st.header("Calorie Burnt During Exercise 🏋️‍♀️")


s1=st.radio("Choose A Gender",["Male","Female"])

s2=st.number_input("Age",1,100,1,1)

s3=st.number_input("Height (in cm's)",10.0,600.0,10.0,1.0)

s4=st.number_input("Weight (in Kg)",20.0,200.0,20.0,1.0)

s5=st.number_input("Duration (in mins.)",1.0,32.0,1.0,1.0)

s6=st.number_input("Heart Rate ",66.0,130.0,66.0,1.0)

s7=st.number_input("Body Temp",36.0,42.0,36.0,0.1)


btn=st.button("Predict")

if btn:
    if s1=="Male":
        s1=0
    else:
        s1=1
    df={
        "Gender":[s1],
        "Age":[s2],
        "Height":[s3],
        "Weight":[s4],
        "Duration":[s5],
        "Heart_Rate":[s6],
        "Body_Temp":[s7],
    }
    df=pd.DataFrame(df)
    print(BestModel.predict(df)[0])
    prediction = round(float(BestModel.predict(df)[0]),2)
    st.subheader(f"The Prediction of your Calories  Is: {prediction}")






