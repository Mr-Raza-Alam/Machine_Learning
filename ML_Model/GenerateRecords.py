'''
Build a binary classification model under supervise learning ,using Logistic Regression Algorithm
'''
import pandas as pd
import random
from datetime import time

# Parameters
merchant_categories = [
    'Grocery', 'Electronics', 'Clothing', 'Restaurants',
    'Travel', 'Fuel', 'Pharmacy', 'OnlineServices'
]
locations = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad',
    'Chennai', 'Kolkata', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow'
]

data = [] #empty list

for i in range(1, 101):
    transaction_id = i
    transaction_amount = round(random.uniform(100, 50000), 2)
    transaction_time = time(
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    ).strftime("%H:%M:%S")
    merchant_category = random.choice(merchant_categories)
    customer_age = random.randint(18, 70)
    customer_gender = random.choice(['Male', 'Female'])
    customer_income = random.randint(10000, 200000)
    transaction_location = random.choice(locations)
    previous_fraud_count = random.randint(0, 5)
    fraud = 1 if random.random() < 0.12 else 0  # ~12% fraud rate
    
    data.append([
        transaction_id, transaction_amount, transaction_time, merchant_category,
        customer_age, customer_gender, customer_income, transaction_location,
        previous_fraud_count, fraud
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'Transaction-id', 'TransactionAmount', 'TransactionTime', 'MerchantCategory',
    'CustomerAge', 'CustomerGender', 'CustomerIncome', 'TransactionLocation',
    'PreviousFraudCount', 'Fraud'
])

# Save CSV
df.to_csv("transactions_100.csv", index=False)
