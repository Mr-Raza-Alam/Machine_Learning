# now here i am going to analyse the data that are avialable in csv file
import pandas as pd
import matplotlib.pyplot as plt

transact_record = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\TransactBill_recorde.csv')
customer_record = pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\Sale_data.csv')

# Handling missing value
# print(transact_record.isnull().sum())  

transact_record['Transaction_id'] = transact_record['Transaction_id'].fillna(transact_record['Transaction_id'].median())
transact_record['Customer_id'] = transact_record['Customer_id'].fillna(transact_record['Customer_id'].mean())
transact_record['Product'] = transact_record['Product'].fillna('T-shirt')
transact_record['Total_Bill'] = transact_record['Total_Bill'].fillna(transact_record['Total_Bill'].min())
transact_record['Quantity'] = transact_record['Quantity'].fillna(transact_record['Quantity'].mean())
transact_record['Transaction_Date'] = transact_record['Transaction_Date'].fillna('05-02-2016')

# print("\n")
# print(transact_record.isnull().sum())

# Remove duplicates element
# print(transact_record.duplicated().sum())
# print(transact_record.info())

#Correcting the dataType
transact_record = transact_record.astype({
  'Customer_id'  : int,
  'Quantity':  int,
  'Total_Bill': float
 })

# print(transact_record.columns)
# print(transact_record.head(6))

# print(transact_record.head(6))

# Validating the data
transact_record = transact_record[transact_record['Quantity']>=0]
transact_record = transact_record[transact_record['Total_Bill']>=0]


# print(transact_record.head(6))

# Data-Exploration
#a- convert date from string format to  dateTime format
transact_record['Transaction_Date'] = pd.to_datetime(transact_record['Transaction_Date'],format='%d-%m-%Y',errors='coerce')
transact_record.to_csv('C:\\Users\\LENOVO\\OneDrive\\Documents\\TransactBill_recorde.csv',index=False)
print("\n")
# print(transact_record.info())

# b - get total no.of  customers in the customer base
# print(customer_record['Customer_id'].value_counts()) # return total no of customer in each category
print(customer_record['Customer_id'].value_counts().sum()) # now it return total summarise record  i.e actually total no. of customer were made transaction

# c- want to know ,total no.of customer who have placed the order
print(transact_record['Customer_id'].nunique()) # return unique customer
# d - merge the both the dataFrames using merger() method
merge_df  = pd.merge(customer_record,transact_record,on='Customer_id',how='inner')
print("After merging two data-frames \n")
# print(merge_df.head(6))
# print(merge_df.info())

#groupby and sum  total no.of item placed by the customer that belongs to the particular group
# summary_age = merge_df.groupby('Age')['Quantity'].sum()
# print(summary_age)

# summary_gender  = merge_df.groupby('Gender').agg({
#     'Quantity': 'sum',
#     'Total_Bill' : 'sum'
# })
# summary_gender['Total_Bill'].plot(kind='bar',figsize=(6,4),title='Total sales by Gender',color='lightgreen')
# plt.show()
# summary_gender['Quantity'].plot(kind='bar',figsize=(6,3),title='Total sales by Gender')# since here no color attribut is added then pandas will display the result in bydefault color
# plt.show()
# print(summary_gender.head())

summary_country  = merge_df.groupby('Country').agg({
    'Quantity': 'sum',
    'Total_Bill' : 'sum'
})

summary_country['Quantity'].plot(kind='bar',figsize=(8,3),title='Total sales by country',color='orange')
plt.show()
# print(summary_country.head())