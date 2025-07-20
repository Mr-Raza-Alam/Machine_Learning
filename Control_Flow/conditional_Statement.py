'''
Condi. State. allow you to execute certain blocks of code
under certain specific conditions.

its syntax 
if statement

'''
temp = 15
if temp >20: # temp >20 is a conditional statement and return boolean value
  print("It's a warm day")
else:
  print("It's a cool day")

  # if - elif and else ,here elif means is else if

age = -23
if  age>18 and age<45:
  print("You are young and eligible to vote")
elif age>45:
  print("You are old")
elif age>0 and age<18:
  print("You are child")
else:
  print("Invalid age")
# Nested Condition

if temp>15:
  if age>50:
    print("It's a hot day,So old people can vote from their home")
  else:
    print("Come to Election Booth and vote")
else:
   print("It's a cool day and everyone can vote easily,So go and vote")

def isLeapYear(year):
   if year %4==0:
     if year%100!=0:
      if year%400 == 0:
        return True
   return False

year = int(input("Enter a year : "))   
isLeap = isLeapYear(year)
if isLeap:
  print(year,f" is a leap year.")
else:
  print(year,f" is a leap year.")
    