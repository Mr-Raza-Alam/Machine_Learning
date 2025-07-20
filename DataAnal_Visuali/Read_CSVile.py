import pandas as pd  # here pd is an alieas of pandas
import os #

# Reading a CSV file into a dataframe

'''
syntax
vari = pd.read_CSV('fileName.CSV')
vari.head()
'''
#print("Looking in : ",os.getcwd())
attandence_record = pd.read_csv('Sale_data.csv')
#so here attandence_record(an object) is a dataframe return pd.read_CSV()
print(attandence_record.head())
print(attandence_record.shape) # return total rows and coloumns that are actually  avialable
print(attandence_record.columns)# return list of structre of dataFram i.e columns Name with dtype = 'Object'