# seaborn with line_chart for data visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# load dataset from csv file i.e the data source
df = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\Sale_data.csv')

# print(df.head(6))

#histogram

plt.figure(figsize=(6,4))

sns.histplot(df['Age'],bins=5,kde=True, color='orange')
plt.title('Distribution over Age')
plt.xlabel('Age')
plt.ylabel('No. of customers')
plt.show()


