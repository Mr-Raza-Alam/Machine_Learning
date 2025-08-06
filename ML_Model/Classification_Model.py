'''
Build a binary classification model under supervise learning ,using Logistic Regression Algorithm
Objective is to
Predict whether a transaction is fraudlent based on various features of the 
transaction.This is a binary classigication problem where the target
variable is 'Fraud',indicating whether a transaction is fraudulent(1) or legitmate(0)
'''
# import all neccessary libraries of python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

import warnings
warnings.filterwarnings("ignore")

# load the dataset from a csv file
df = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop\\PythonProg\\ML_Model\\transaction_Records.csv")
# df = pd.read_csv('transaction_Records.csv')
# display the first few record to verify that the dataset is loaded
# print(df.head())
# print(df['TransactionTime'].dtype)

#essenetial Exploratory Data Analysis(EDA)

# summary statistics
# print(df.describe())

# check for  missing values
# print(df.isnull().sum())

#Distribution of target Variable i.e fraud

# sns.countplot(x='Fraud',data=df)
# plt.title('Distribution of Fraudlent Transaction')
# plt.show()


# Distribution of Transaction Amount by Fraud status,using Histogram

# sns.histplot(data=df,x='TransactionAmount',hue='Fraud',multiple='stack',bins=10)
# plt.title('Transaction Amount Distribution by Fraud Status')
# plt.show()

# Distribution of  transacion Amount over box plot based on fraud status

# sns.boxplot(x='Fraud',y='TransactionAmount',data=df,color='green')
# plt.title('Distribution of Transaction Amount over Fraud Status')
# plt.xlabel('Fraud')
# plt.ylabel('Trans.Amt.')
# plt.show()

# HeatMap distribution for the dataset ,and for this we require correlationMatrix and for to find correlation Matrix we required .corr()method that works only numerical data
# num_cols = () # an empty tuple ,use to collect columns having numerical values across its column
# for col in df.columns:
#     if df[col].dtype != object:
#         num_cols.append(col)

# correlation_Matrix = df[num_cols].corr()

# sns.heatmap(correlation_Matrix,annot=True,cmap='coolwarm',fmt='.3f')
# plt.title('Correlation Matrix Distribution over dataSet')
# plt.show()

# Data Preprocessing 

label_encoders = {} # this is for mapping non-numerical columns by some label for each column's values

for col in ['TransactionTime','MerchantCategory','CustomerGender','TransactionLocation']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features & target

X = df.drop(['Transaction-id','Fraud'],axis=1)
Y = df['Fraud']
# now our dataset is ready to split into train and test set
# print(X.head())
# print('\n',label_encoders)

# Now its time to split the dataSet into training and testing set

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.4,random_state=7)

#Feature Scaling
scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)
# now we have the dataSet that i requried for data modeling

# Logistic Regression Algorthim
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(x_train,y_train)

logreg_pred = logreg.predict(x_test)
logreg_accuracy = accuracy_score(y_test,logreg_pred) # it gives the accuracy score of the model over its predicted values

# Display the accuracy and perform other metric for Evaluatin performance of the created model

# print(f"Logistic Regression model accuracy : {logreg_accuracy*100:.2f}%")
# print('\nLogReg Classification Report\n')
# print(classification_report(y_test,logreg_pred))

# Visualize the predicted result over actual value

# correlation_Matrix = X[X.columns].corr()
# sns.heatmap(correlation_Matrix,annot=True,cmap='coolwarm',fmt='.3f')
# plt.title('Correlation Matrix Distribution over dataSet')
# plt.show()
plot_df = X.copy()
plot_df['Fraud'] = Y
plt.figure(figsize=(10,6))
sns.histplot(data=plot_df,x='TransactionAmount',hue='Fraud',multiple='stack',bins=10)
plt.title('Transaction Amount Distribution by Fraud Status')
plt.show()