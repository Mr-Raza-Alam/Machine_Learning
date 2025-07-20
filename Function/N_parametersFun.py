'''
using * asterik symbol ,can pass no. of arguments
def fun(*var): -- this is a general definition to no. of argument and can iterable

So,
*args ALLOWS a fun. to accept a variable no. of poitional
 arguments as a tuple
 It enables you to call a function with more arguments than
 the number of formal parameters defined,making your fun.
 flexible and adaptable.
'''

def sum(*numbers): # here the collection numbers will be a tuple
    s = 0
    for number in numbers:
        s +=number
        if number == 5:
         print("Yes 5 exist")
         s -=5
         return s
    return s

print(f"Sum of 6 numbers : ",sum(8,7,6,5,0,9))

