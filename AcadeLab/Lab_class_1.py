# q1 frequency of integer array

def frequencies(nums):
     nums.sort() # in-place sorting 
     rept = nums[0]
     i = 1
     c = 1
     counts={} #empty dict
     while i<len(nums
                 ):
        if(nums[i] == rept):
            c +=1
            rept = nums[i]
        else:
            counts[rept] = c
            c = 1
            rept = nums[i]
        i +=1
     counts[rept] = c
     return counts

nums = [2,4,5,6,2,4,5,1,3,1,2,1,5,2] 
# print('original list : ',nums,'\nFrequencies of each element of list are')           
# print(frequencies(nums))

#q2 GCD of 2 numbers

def getGCD(n1,n2):
    gcd = -1
    for i in range(2,min(n1,n2)+1):
        if (n1%i == 0) and (n2%i == 0):
           gcd = i   
    return gcd 

# n1 = int(input("Enter 1st number : "))
# n2 = int(input("Enter 2nd number : "))
# print(getGCD(n1,n2))
                
#q3 reverse each word in a string 

# to convert integer to string  the use str(x), it return x in string form where x = integer 

def reverseEachWord(str1):
     word_list = str1.split()
     rev_str = ""
     for i in word_list:
         rev_word = i[::-1]
         rev_str +=rev_word + " "
     return rev_str
         
# string = input("Enter a string : ")
# print(reverseEachWord(string))

#q4
def countCharacter(str1):
    count = [0,0,0]
    for i in str1:
        if i.isalpha():
            count[0] +=1
        elif i.isdigit():
            count[1] +=1
        else:
            count[2] +=1
    res = {
        'letters': count[0],
        'digits' : count[1],
        'others' : count[2]
    }
    return res
# string = input("Enter a string : ")
# print(countCharacter(string))         

''' 
q5 concatenate 2 Strings in the following formats
   input : st1 = 'abc',st2 = 'pqr;
   output : arbqcp
'''

def concateStrs(st1,st2):
    res = ''
    if len(st1)>=len(st2):
        i , j = 0,len(st2)-1
        while i<=j:
            res +=st1[i]+st2[j]
            i +=1
            j -=1
        # now for remaining characters of string st1
        while i<len(st1):
            res +=st1[i]
            i +=1
    else :
        i , j = 0,len(st2)-1
        while i<=j:
            res +=st1[i]+st2[j]
            i +=1
            j -=1
        # now for remaining characters of string st2
        while j>=0:
            res +=st2[j]
            j -=1
    return res

st1 = input('Enter 1st string : ')
st2 = input('Enter 2nd string : ')

print('\nAfter concatenation of 2 strings are : ',concateStrs(st1,st2))
print()
