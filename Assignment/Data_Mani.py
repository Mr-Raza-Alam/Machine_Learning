'''
Instruction 2 : Data Maniputlation with Pandas
'''
import pandas as pd

#Task 1 : Creating and Exploring a DataFrame
data = {
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Age':[25,38,35,40,45],
    'City':['New York','Los Angeles','Chicago','Houston','Phoenix']
}

# #1
df = pd.DataFrame(data)
# #2
# print(df,"\n")
# #3
# Avg_Age= df['Age'].mean()
# print(f"Average age of person : ",Avg_Age,"\n")

#Task 2: Filtering and Aggregation

#1
df = df[df['Age']>30]
print(df,"\n")
#2
df['AgeGroup'] = df['Age'].apply(lambda a:'Senior' if a>=40 else 'Adult')
print(df)
#3
group_summary = df.groupby('AgeGroup')['Age'].mean()
print("\n",group_summary)
