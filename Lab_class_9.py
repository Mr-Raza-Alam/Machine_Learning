#  Set of max values of the set of sub-array of given size from the given array

def maxValue(arr,k):
    res = []
    for i in range(len(arr)):
        m = 0
        t = i
        while t < k+i:
           if t<len(arr):
               m = max(m,arr[t])
           t +=1
        if t==len(arr):
           res.append(m)            
           return res
        res.append(m)

arr = [5,7,2,1,2,5,7]
k = int(input('Enter a positive integer K : '))
print('The list of max values of all possible contingous sub-array of given array is given below \n',maxValue(arr,k))


