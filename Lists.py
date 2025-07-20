'''
lists are used to store collections of items,
which can of any type.
Lists are ordered , mutable, and can contain duplicate elements
'''
'''
  syntax var_name = []
'''
empty_list = []
 
# skill list
skills = ["Html","Css","JS","Java","Python","C++","C","NodeJs","React"]

# phone list
phoneNumbers = ["91+ 7004891854","91+ 8984567009","91+ 8785432110",]

# anonymous details
anonymousDetails = ["Anonymous",8590321232,"anon342@gmail.com",23,67.8,True]

# Access the items
# syntax listName[0] return first actual element like 0th based index array
print(skills[5])
#slicing th list and its syntax listName[si:ei](ei is exclusive)

print(anonymousDetails[0:]) # return whole list in this [] form
# but 
print(phoneNumbers[:4]) # return items from idx = 0 to idx = 3

# and if
print(skills[3:7]) # return items from idx = 3 to idx = 6


# Methods of LIST

#  .append(only value) add to last to the list
skills.append("MongoDB")
print(skills[3:])
#  .insert(idx,value)
skills.insert(2,"Bootstraps")
print(skills[0:3])

# .remove(value)
phoneNumbers.remove("91+ 7004891854")
print(phoneNumbers[0:])
# .pop() -- remove last item from the list
anonymousDetails.pop()
print(anonymousDetails[1:])