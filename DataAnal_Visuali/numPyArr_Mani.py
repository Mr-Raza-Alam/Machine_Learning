'''
using indexing and slicing technique , here we access the elemennt or the data from the numpy ARRAY  where the collection of data are stored
'''
import numpy as np

# arr_1d = np.array([5,3,2,7,3,8])
# print(arr_1d[arr_1d>5]) # here actually no real indexing value ,it is a boolean value that takes only such element which satisfied the condition

# print("\n")
# print(arr_1d)

arr_2d  = np.array([[10,20,30],[60,70,55],[32,67,89],[10,23,56]])
# print(arr_2d[3,[0,2]]) # this is integer array indexing

# print(arr_2d[:2,:2]) # it return first 2 rows and columns
# print(arr_2d[::1])
# print()
# print(arr_2d[:,::1])

check_arr = np.linspace(1,5,5)
print(check_arr)