#Instruction 1. python programming Basics 

#Task 1: Python Function and Lists


# sq = lambda x: x**2 # it is like as sq(x)--> return x**2
# def square(numbers):
#     return list(map(sq,numbers))

# # Test 1
# nums1 = [2,4,5,6,7,8,12,-4,0.7,1,14,0.3]
# nums2 = [-1,-3,-0.6,0,4,6,8,0.8,9,10]
# print(square(nums1))
# print("\n")
# print(square(nums2))


#Task 2 : Dictionary operation & Comprehenssions

#1
stu_mark = {
    'Akram':78,
    'Bhumika':79,
    'Chunky': 36,
    'Daniel': 47,
    'Elinna': 86,
    'Farhan': 93,
    'Gyatari':70,
    'Harsh' : 41,
    'Illa' : 38,
    'Juli' : 44
}

#2
def getNewList(stu_mark):
    return {name:mark for name,mark in stu_mark.items() if mark>50}

#3
newStu_mark = {name: mark*1.1 for name,mark in stu_mark.items()}

print(getNewList(stu_mark))

print()
print(newStu_mark)