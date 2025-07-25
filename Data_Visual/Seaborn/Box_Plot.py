# This is for boxPlot element for data visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# load dataset from csv file i.e the data source
df = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\TransactBill_recorde.csv')

# print(df.head())

# Box plot
plt.figure(figsize=(8,4))

sns.boxplot(x='Product',y='Quantity',data=df,palette='pastel')
plt.title('Distribution over Product and Quantity')
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.show()