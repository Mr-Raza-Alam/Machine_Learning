'''
 UDF are blocks of code designed to perform specific tasks by an user

 its syntax
 def FunName(): -- used to define a fun.
 
 UI(user-input)
  using input()-- it return a string and the text inside it ,is a prompt shown to the user
   dataType(input(...)) using type casting convert string value to the corresponding dataTYPE
'''
#Greet
def greet(Name):
    print(f"Hi, Mr.",Name," Welcome to the session")
# calling a function
name = input("Enter your name : ")
greet(name)

# Multiplication of 2 real numbers
def multiply(a,b): # funt.(parameters)
    return a*b
print()
a= int(input("Enter 1st number : "))
b= int(input("Enter 2nd number : "))
print(a,"x",b," = ",multiply(a,b)) # while calling a fun(argument)