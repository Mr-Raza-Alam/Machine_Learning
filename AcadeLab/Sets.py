'''
Sets are a built-in data structure that represent an unordered
collection of unique elements

why do we need to learn sets ??
Ans --  it is b/c , the set contains only unique elements in it and in unorder
and python has ability to remove duplicates value while 
insert duplicate values in set data structure .

This is particularly useful for operations involving 
membership testing,removing duplicates,and 
mathematical set Operations.

properties of set data-structure

i) contain unique elements only
ii) remove duplicate element if exist
iii) access by using for loop i.e 
for varName in set_Name:
iv) mutable in nature

its syntax
set_var = {}
'''
empty_set = {}

#friend set
friends = {"Alice","Bob","Carry","Dean","Elice"}
print(type(friends))
print(friends)

#modify
friends.add("Alice") # will automatically remove
friends.update(["Akram","Ali","Bikash"])
friends.remove("Elice")
#Access the item of the set
# so for this , it doesn't have any notation,it is done by using loop
for ele in friends:
    print(ele)
