import pandas as pd
from sklearn.naive_bayes import GaussianNB
import streamlit as st

# Load the CSV file into a pandas dataframe
st.set_page_config(page_title="Diabetes Prediction")
df = pd.read_csv('diabetes2.csv')
st.title("Diabetes Prediction Using Classification")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/1567677.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# Accept user inputs for the feature columns
pregnancies = st.number_input('Pregnancies',step=1)
glucose = st.number_input('Glucose')
blood_pressure = st.number_input('Blood Pressure')
skin_thickness = st.number_input('Skin Thickness')
insulin = st.number_input('Insulin')
bmi = st.number_input('BMI')
dpf = st.number_input('Diabetes Pedigree Function')
age = st.number_input('Age',step=1)

# Use the model to make predictions on the user inputs
model = GaussianNB()
model.fit(df.drop('Outcome', axis=1), df['Outcome'])
prediction = model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

# Display the prediction to the user
if prediction[0] == 0:
    st.write('Prediction: Not Diabetic')
else:
    st.write('Prediction: Diabetic')
