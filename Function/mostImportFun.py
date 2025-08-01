'''
Lambda, Map, and Zip functions

These fun. provide powerful ways to handle data and 
perform operations concisely .

lambda fun. is an anonynous function
syntanx
 lambad paramerters : expression(only 1 )
'''
#lambda a,b,c : a * b + c 

square = lambda x : x**2 # to get square

number = int(input("Enter a number : "))
print(f"Square of ",number," = ",square(number))

print()

#Zip function 
'''
  use of Zip fun.,
  case : when you have data given in multiple objects
  or have diff. kind of containers for your data
'''
# Some employees
first_NAMEs = ["John","Marry","Bob"]
last_NAMEs = ["Smith","Jane","Smith"]

#full_NAMEs = zip(first_NAMEs,last_NAMEs)
#so as zip() return directly zip object with its location
#And to get the actual value needs to convert into list type b/c zip(list1,list2) contains list-items
full_NAMEs = list(zip(first_NAMEs,last_NAMEs)) # now it return list of tuples where each tuple contain (first,last)Name
print(full_NAMEs) 

#Map function
'''
it helpful to apply iteration a function based on objects
 or iterable objects like list,tuple,set,dictionary
'''
print()
numbers = [2,3,4,5,6]
#square_Numbers = map(square,numbers) # it also return map object with its location 
# to get value of each number parse it to list
square_Numbers = list(map(square,numbers)) # it return list of number
print(square_Numbers)