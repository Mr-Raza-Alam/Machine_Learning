#1 divide the given list into chunks of size n
def divideList(nums,n):
    ans = []
    i = 0
    while i<len(nums):
        curr = []
        for j in range(i,n+i):
            if (i+n-1)<len(nums):
                curr.append(nums[j])
        ans.append(curr)
        i +=n
    return ans

nums = [2,3,5,2,1,6,5,2]
# chunkSize = int(input("Enter the size of chunk : "))
# print('Origianl list : ',nums,'\nAfter dividing list into chunk of size ',chunkSize)
# print(divideList(nums,chunkSize))

#q4 Reverse a list , so my approach is using 2 pointers
def reverse(nums):
    st = 0
    end = len(nums)-1
    while(st<=end):
        #swapp(nums[st],nums[end])
        nums[st],nums[end] = nums[end],nums[st]
        st +=1
        end -=1
    return nums
nums = [2,3,5,2,1,6,5,7]
# print('Origianl list : ',nums,'\nAfter reverse its element list is')
# print(reverse(nums))

#q5 find a given key is exit in the list
def searchKey(nums,key):
    for i in nums:
        if key == i:
            return True
    return False
nums = [2,3,5,2,1,6,5,7]
# key = int(input("Enter a required key : "))
# print('Original list ',nums,'\nFind ',key,'in the above list.')
# print(key,f" is found") if searchKey(nums,key) else print(key,f" is not found") # this is ternary operator

#q7 find remainder of array multplication divided by a number n
def remList(nums,n):
    rem = []
    for i in nums:
        rem.append(i%n)
    return rem
nums = [2,3,5,2,1,6,5,7]
# n = int(input("Enter a common divisor : "))
# print('Original list ',nums,'\nAfter division list is :')
# print(remList(nums,n))
              
#q4 Commulative sum of list

def commulativeSum(nums):
    ans = []
    s = 0
    for i in nums:
        s +=i
        ans.append(s)
    return ans

nums = [7,6,2,0,1,4]
print('Original List: ',nums,'\nIts Commulative Sum : ')
print(commulativeSum(nums))
