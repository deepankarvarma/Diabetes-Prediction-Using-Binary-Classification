import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import seaborn as sns 
import matplotlib.pyplot as plt

# Load the CSV file into a pandas dataframe
df = pd.read_csv('diabetes2.csv')

# Making a count vs outcount plot to check the balance in data 
# sns.catplot(x="Outcome", kind="count", data=df, palette="Set2")
# plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Outcome', axis=1), df['Outcome'], test_size=0.2, random_state=42)

# Create a linear regression model and fit it to the training data
model = GaussianNB()
model.fit(X_train, y_train)

# Use the model to make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy=accuracy_score(y_test, y_pred)
print(f"Classification Accuracy:\n {accuracy}")

data = [[5, 150, 33.7, 50, 150, 74, 0.5, 53]]

# Create the pandas DataFrame 
df_test = pd.DataFrame(data, columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])

# Predict on new data
res = model.predict(df_test)
print(res)