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