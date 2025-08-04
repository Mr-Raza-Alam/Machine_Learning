import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\housing_data.csv")

print(df.head())

X = df[['medInc','HouseAge','AvgRoom','AvgOccup','latitude','longitude']]
Y = df['Price']

#split the dataSet into training and testing Set
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

#create and train the model
multi_model = LinearRegression()
multi_model.fit(X_train,y_train)

# Predict the test output
y_pred = multi_model.predict(X_test)

# Evaluate the  model
print(f'\nMean Square Error : {mean_squared_error(y_test,y_pred)}')
print(f'\nR^2 score : {r2_score(y_test,y_pred)}')


# display the coefficients of the model
coefficient = pd.DataFrame(multi_model.coef_, X.columns, columns=['Coefficient'])

print("\n")
print(coefficient)


