'''
For loops are used to iterate over a sequence(like a list,
tuple,or string,or other iterable objects)

They allow you to execute a block of code multiple
times with different values from the sequence
 
its syntax
for tempVariable in(keyward) iterableObjectName
'''

fruits = ["apple","mango","banana"]
i = 1
weekDays = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print()
for day in weekDays:
    print(f"day-",(i),day)
    i +=1
print()

for fruite in fruits:
    print(fruite)
print()
 # a method called range(end-value) -return a list of number from 0 to end-value-1
 # originally range(start-value(optional),end-value)
for num in range(5,15):
    print(num)