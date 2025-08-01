#Instruction 1. python programming Basics 

#Task 1: Python Function and Lists


# sq = lambda x: x**2 # it is like as sq(x)--> return x**2
# def square(numbers):
#     return list(map(sq,numbers))

# # Test 1
# nums1 = [2,4,5,6,7,8,12,-4,0.7,1,14,0.3]
# nums2 = [-1,-3,-0.6,0,4,6,8,0.8,9,10]
# print(square(nums1))
# print("\n")
# print(square(nums2))


#Task 2 : Dictionary operation & Comprehenssions

#1
stu_mark = {
    'Akram':78,
    'Bhumika':79,
    'Chunky': 36,
    'Daniel': 47,
    'Elinna': 86,
    'Farhan': 93,
    'Gyatari':70,
    'Harsh' : 41,
    'Illa' : 38,
    'Juli' : 44
}

#2
def getNewList(stu_mark):
    return {name:mark for name,mark in stu_mark.items() if mark>50}

#3
newStu_mark = {name: mark*1.1 for name,mark in stu_mark.items()}

print(getNewList(stu_mark))

print()
print(newStu_mark)

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

'''
Instruction 3 : Data Manipulation with NumPy
'''
import numpy as np

#Task 1: NumPy Array Operations

#1
# arr_1d= np.linspace(1,50,12) # 12 random value b/w 1-50
# print(arr_1d,"\n")
# #2
# matrix = arr_1d.reshape(3,4) # matrix []3x4 size
# print(matrix)
#3
def max(arr_1d):
    max = -1
    for ele in arr_1d:
        if(max<ele):
            max = ele
    return max

def min(arr_1d):
    min = 60 # since array has value range i.e 1-50
    for ele in arr_1d:
        if(min>ele):
            min = ele
    return min

def avg(arr_1d):
    sum = 0
    for ele in arr_1d:
        sum +=ele
    return sum/len(arr_1d)

# print("Maximum values of the array = ",max(arr_1d))
# print("\nMinimum values of the array = ",min(arr_1d))
# print("\nAverage values of the array = ",avg(arr_1d))


#Task 2 : Array Indexing and Slicing

#1
arr_2d= np.arange(1,13).reshape(4,3)
print(arr_2d,"\n")
#2
second_row = arr_2d[1]
print(second_row)
#3
subMatrix = arr_2d[:2,:2] # row's range [0,2) and col's range [0,2)
print(subMatrix)