'''
Classes
These are blueprints for creating objects in OOP,encapsulating
data and method that operate on that data.

in simple word
Classes allow you to bundle data and functionality together
making it easier to manage and reuse code.

class CLASSName:
 def __init__(self,para1,para2): -- act as construction will help to construct an object of the class
  self.para1 = para1
  self.para2 = para2
  here self is basically refereence to the current object being created
'''

#Human class
class Human:
    def __init__(self,name,age): #construnctin
        self.name = name #Attributes 1
        self.age = age #Attributes 2

    def walk(self):
        print(f"{self.name} is walking")
    def talk(self):
        print(f"{self.name} is talking")

#create object
h1 = Human("John",27) 
h2 = Human("Alice",45)
print(h1.talk())
print(h1.walk())

class Cirle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    def circumference(self):
        return 2*(3.14*self.radius)
    
c1 = Cirle(4)
c2 = Cirle(3.2)
print()
print(c1.area())
print()
print(c2.circumference())


        