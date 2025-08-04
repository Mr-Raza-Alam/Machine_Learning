# Regression Model using Linear Regression Algorithm

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

import warnings
warnings.filterwarnings("ignore")

#Read a CSV file data i.e a data source which given machine data for analysis and prediction after learning the pattern from the given dataset

#load data
df = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\housing_data.csv")
# print(df.head())
#Exploratory for Data Analysis
# get df info
# print("\tHouse_Data Information\n")
# print(df.info())

#get df's description = all statistical value
# print()
# print(df.describe())

# Data visualization to understand the relationship b/w variables

# PairPlot
# plt.figure(figsize=(9,5))
# sns.pairplot(df,diag_kind='kde')
# plt.show()

#Heat-Map(Correlation matrix)
# correlation_matrix = df.corr()
# print(correlation_matrix) # it print a sqaure matrix of size 7x7 
# sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',fmt='.3f')
# plt.title("Correlation Matrix")
# plt.show()
# print(plt.colormaps()) it return a list of color used in heatmap

#histogram for individual records
# plt.hist(df,bins=8,color=['green','purple','orange','cyan','magenta','brown','red'],edgecolor='black')
# plt.title("House Records")
# plt.show()

#boxplot 
# plt.figure(figsize=(12,10))
# for i,col in enumerate(df.columns):
#     plt.subplot(3,3,i+1)
#     sns.boxplot(df[col])
#     plt.title(col)
# plt.tight_layout()
# plt.show()

# Main work - Simple Linear Regression

#Define the target and predictor variable
X = df[['medInc']] # indepedent variable or Predictor
Y = df[['Price']] # dependent variable or target

# split the dataset into training and testing set
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

# Create and train the model
simple_model = LinearRegression() # since it is a class,but while using it make sure class()
simple_model.fit(X_train,y_train) # since it is a supervise linear Regression model so, X_train - characteristic of data , and y_train = label data
#now the model will learn the pattern from these training data and will predict some output based on given testing data

# Predictions
y_pred = simple_model.predict(X_test) # so here y_pred = predicted target, and X_test = predictor
# print(y_pred)

#Evaluate the model
# print(f'Mean Square Error = {mean_squared_error(y_test,y_pred)}')
print()
# print(f'R^2 score = {r2_score(y_test,y_pred)}') # here r2_score() internally calculate its value based on the given formula i.e R^2 = 1-RSS/TSS

# Plot the regression line

# plt.figure(figsize=(9,6))
# plt.scatter(X_test,y_test,color='green',label='Actual data')
# plt.plot(X_test,y_pred,color = 'purple',linewidth=2,label='Regression line')
# plt.xlabel('Median Income')
# plt.ylabel('Price')
# plt.legend()
# plt.show()

#now test for unseen data point
#Assuming the model has already been trained and the relevant libraries have been imported
# Input medInc value from the user
medInc_Value = float(input("Enter a median income : "))

#convert the input value to a 2d array for prediction
medInc_array = np.array([[medInc_Value]])

# Predict the house price using the trained model
predicted_res = simple_model.predict(medInc_array)

# Output the prediction
print(f'The predicted house price for MedInc value of {medInc_Value} is : ${predicted_res[0].item():.2f}')
