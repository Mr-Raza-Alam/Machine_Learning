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

# nums = [2,3,5,2,1,6,5,2]
# chunkSize = int(input("Enter the size of chunk : "))
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
# nums = [2,3,5,2,1,6,5,7]
# print(reverse(nums))

#q5 find a given key is exit in the list
def searchKey(nums,key):
    for i in nums:
        if key == i:
            return True
    return False
# nums = [2,3,5,2,1,6,5,7]
# key = int(input("Enter a required key : "))
# print(key,f" exit") if searchKey(nums,key) else print(key,f" not exit") # this is ternary operator

#q7 find remainder of array multplication divided by a number n
def remList(nums,n):
    rem = []
    for i in nums:
        rem.append(i%n)
    return rem
# nums = [2,3,5,2,1,6,5,7]
# n = int(input("Enter a common divisor : "))
# print(remList(nums,n))
              
