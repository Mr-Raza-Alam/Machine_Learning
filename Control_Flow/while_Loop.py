'''
while loops are used to repeatedly execute a block of code
 as long as a specified condition remains true.

They are useful when the number of iterations is unknown
beforehand and depends on dynamic conditions

its syntax

'''
#  using while loop
number = 10
RealNum = 5
while number>0:
    print(RealNum,f"X",number,f" = ",(RealNum*number))
    number -=1
print("\n")
number += 3
# use of break statement
while number>0:
    if number ==2:
        print("its time to break")
        break
    else:
        print(number)
    number -=1
