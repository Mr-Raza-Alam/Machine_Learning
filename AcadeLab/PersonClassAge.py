'''
 Classes and instance in Python
'''
from datetime import date
#q1.
class Person:
    today = date.today()
    def __init__(self,n,c,dob): # constructor,used to construct an object of the class Person
        self.name = n
        self.country = c
        self.DOB = dob
    def leap(self,y):
      return y%400 == 0 or (y%4 == 0 and y%100 !=0 )

    def getAge(self):
        age = []
        if  self.leap(self.today.year) and self.today.month == 2:
            day = self.today.day - self.DOB[0]
            if day>0:
                age.append(day)
            else:
                self.today.day +=29
                self.today.month -=1
            month = self.today.month - self.DOB[1]
            if month>0:
                age.append(month)
            else:
                self.today.month +=12
                self.today.year -=1
            year = self.today.year - self.DOB[2]
            age.append(year)
            return age
        else: # if no leap year + leap year without feb month 
            day = self.today.day - self.DOB[0]
            if day>0:
                age.append(day)
            else:
                if self.today.month in [4,6,10,11]:
                    self.today.day +=30
                    self.today.month -=1
                elif self.today.month in [1,3,5,7,8,10,12]:
                    self.today.day +=31
                    self.today.month -=1
                else:
                    self.today.day +=29
                    self.today.month -=1
            month = self.today.month - self.DOB[1]
            if month>0:
                age.append(month)
            else:
                self.today.month +=12
                self.today.year -=1
            year = self.today.year - self.DOB[2]
            age.append(year)
            
            return f"And Your age is {age[2]}years,{age[1]}months,{age[0]}days"

# general form 
name = input('Enter your name .... : ')
country = input('Enter your country name : ')
dob = list(map(int, input("Enter DOB (dd mm yyyy): ").split()))

print('Date of birth : ',dob)
p1 = Person(name,country,dob)
print('Hi,Mr/Miss,',name);print('Your are from ',country); print(p1.getAge())


    
