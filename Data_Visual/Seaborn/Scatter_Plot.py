# This is for scatter plot visaul element for data visaulization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# load dataset from csv file i.e the data source
df = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\Sale_data.csv')

# print(df.head())

# Scatter plot

plt.figure(figsize=(8,4))

sns.scatterplot(x='Customer_id',y='Age',data=df,hue='Gender',palette='pastel')
plt.title('Relationship b/w Customer & Age')
plt.xlabel('Customer_id')
plt.ylabel('Age')
plt.show()

