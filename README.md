# Diabetes Prediction Using Naive Bayes Classifier
This repository contains code for building a model that finds the relationship between the features of a patient and the associated outcome (diabetic or non-diabetic). The code uses a Gaussian Naive Bayes classifier model to classify patients as diabetic or non-diabetic.<br>
### Dataset
The dataset used in this project can be found on Kaggle at https://www.kaggle.com/datasets/kandij/diabetes-dataset. The dataset contains information about patients, including their glucose level, blood pressure, BMI, and other medical details. <br>
### Usage
To run the code, simply run the `model.py` file. The code will load the diabetes dataset, split the data into training and testing sets, and create a Gaussian Naive Bayes classifier model. The model is then trained on the training data and used to predict the outcomes of the testing data. Finally, the accuracy of the model is evaluated and printed to the console.<br>

You can also visit the website hosted on Streamlit at https://deepankarvarma-diabetes-prediction-using-regression-app-3h8wq7.streamlit.app/. The website allows you to enter medical details about a patient and get a prediction about whether they are diabetic or non-diabetic.<br>
### Requirements
The code was written in Python 3. The following Python libraries are required:
<br>
1. pandas<br>
2. sklearn<br>
3. seaborn<br>
4. matplotlib<br>
5. streamlit<br>
### Running the Code
To run the code, simply run the `model.py` file. The code will load the diabetes dataset, split the data into training and testing sets, and create a Gaussian Naive Bayes classifier model. The model is then trained on the training data and used to predict the outcomes of the testing data. Finally, the accuracy of the model is evaluated and printed to the console.
<br>
To run the website, use the following command:<br>

 `streamlit run app.py`
 
 This will start the Streamlit server and open the website in your default web browser. From there, you can enter medical details about a patient and get a prediction about whether they are diabetic or non-diabetic.
