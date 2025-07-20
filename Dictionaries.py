'''
dictionaries are a built-in advance data structure ,used
to store key-value pairs

They are ordered collections where each key is unique and 
is used to map a value
it is mutable in nature

its syntax 
dict_name = {'key' : value,}
'''

empty_dict = {}

# dict for the  student details
student = {
       'name' : "Rommy",  # item1
        'age' : 22,  #item2
        'phNo' : 7941854,
        'profession': "SWE",
        'salary':'$....../in dollar' #item3
    }

#print(student)

#Access the item
# dictName['key'] --return key corresponding value
print(f"Student-Name : ",student['name'])
print()
print(f"")
#Modify dictionary
student['age'] = 20
student['city'] = "Delhi"
print(f"Student-city : ",student['city'])
print(f"Age : ",student.get('age'))

# common operation on dictionaries

#dictName.keys() --- return list of keys exits in dict. prefix with dict_keys()
print(student.keys())
print() # print a blank line or use \n to print nextline
# dictName.values() -- return the list of values of each key prefix with dict_values()
print(student.values())
print()
# dictName.items() -- return a list of tuples/item prefix with dict_items()
print(student.items())