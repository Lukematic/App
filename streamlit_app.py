#load the packages
import streamlit as st
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np
#title for the app
st.title('Predicting student ELPAC scores')
import pickle
data= pd.read_csv('https://raw.githubusercontent.com/OscarG-DataSci/ADS-599B/main/Data%20Folder/new_elpac.csv')
# load model
best_model =  GradientBoostingClassifier()
best_model.load_model("best_model.json")
#show df
if st.checkbox('Show dataframe'):
    data
st.subheader("Please select relevant features of your Student!")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.radio(
        'grade_student:',
        np.unique(data['GradeLevel']))
input_Length1 = st.slider('Vertical length(cm)', 0.0, max(data["TotalAssesments"]), 1.0)
input_Length2 = st.slider('Diagonal length(cm)', 0.0, max(data["DaysAttended"]), 1.0)
input_Length3 = st.slider('Cross length(cm)', 0.0, max(data["ExpectedAttendanceDays"]), 1.0)
input_Height = st.slider('Height(cm)', 0.0, max(data["OverallScore"]), 1.0)
input_Width = st.slider('Diagonal width(cm)', 0.0, max(data["GradeLevel"]), 1.0)
if st.button('Make Prediction'):
    input_species = encoder.transform(np.expand_dims(inp_species, -1))
    inputs = np.expand_dims(
        [int(input_species), input_Length1, input_Length2, input_Length3, input_Height, input_Width], 0)
    prediction = best_xgboost_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Your fish weight is: {np.squeeze(prediction, -1)} Gram")