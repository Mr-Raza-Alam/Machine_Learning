# Data cleaning -- like Handling missing value, remove Duplicates, Correct dataType, Filtering Outliers, Validating data , Consolidation

import pandas as pd

customer_record = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\Sale_data.csv')
print(customer_record.head(4))
# print(customer_record.isnull().sum())
print("\n")
# Handling missing value   -  fill NAN value with median of dataset of respective column 

# customer_record['Age'] = customer_record['Age'].fillna(customer_record['Age'].median())
# customer_record['Balance'] = customer_record['Balance'].fillna(customer_record['Balance'].mean())
# customer_record['Country'] = customer_record['Country'].fillna('India')
# customer_record.to_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\Sale_data.csv',index=False)
# print(customer_record.isnull().sum()) # called to verify that the missing value is filled up or not 

# remove Duplicates value
print(customer_record.duplicated().sum())
print(customer_record.info())
customer_record = customer_record.drop_duplicates()
print("\nAfter removing duplicate rows")   
print(customer_record.info())


