import pandas as pd

# attendence = pd.read_excel('C:\\Users\\LENOVO\\OneDrive\\Documents\\Attendence.xlsx',sheet_name='Sheet1')
# print(attendence.head())

# customer_record = pd.read_excel('C:\\Users\\LENOVO\\OneDrive\\Documents\\customer_data.xlsx',sheet_name='customer_data')
customer_record = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\Sale_data.csv')
print(customer_record.head(7)) # return first 7 records from dataFrame i.e customer_record
# print(customer_record['Gender'].unique())
# print(customer_record['Gender'].value_counts())
print()
print(customer_record.isnull().sum())
print("\n")
print(customer_record.info())
# print(customer_record.describe())