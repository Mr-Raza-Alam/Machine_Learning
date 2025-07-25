# This is for ploting scatter plot using pairplot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# load dataset from csv file i.e the data source
df = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\Sale_data.csv')

# print(df.head())

# pairPlot 
plt.figure(figsize=(8,4))

sns.pairplot(df[['Customer_id','Age','Gender','Country','Balance']],diag_kind='kde',hue='Gender')
# plt.title('Pair relation over Gender')
plt.show()
