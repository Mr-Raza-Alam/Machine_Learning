# print the following patterns
'''
input : 'oranges'
expected output :
      o
      a r
      e g n
      . . . s

my Approach :-  using nested list and and loop with some string,,list methods and assignment operator
'''
def printPattern(st):
   ans = []
   idx ,size = 0,1
   while idx<len(st):
      curr = list(st[idx:idx+size])
      idx +=size
      while len(curr)<size:
         curr.append('.')
      ans.append(curr)
      size +=1
   
   for grp in ans:
     for ch in reversed(grp):
       print(ch,end=" ")
     print()

# st = input("Enter a string : ")
# printPattern(st)


   
''' 
q2.) check if str2's characters are stay in str1 string with same order
e.g
Test -1
input : str1 = 'What is the matter',str2 = 'Water'
output : True

Test -2
input : str1 = 'Hello Techy',str2 = 'HiTech'
output : False
'''

def checkChInOrder(str1,str2):
   k = 0
   for ch1 in str1:
      isC = 0
      if ch1 == str2[k]:
         k +=1
         isC = 1
      if k==len(str2) and isC == 1:
        return True
   return False

# str1 = input("Enter a string : ")
# str2 = input("Enter another string : ")
# print(checkChInOrder(str1,str2))

'''
q3.) Check for the validation of braces
    Test 1
    input : {[(]}
    output : False
 
    Test 2
    input : [({})]
    output : True
'''

def isValid(s):
   if len(s) == 1:
      return False
   st = []
   for i in s:
      if i == '{':
         st.append('}')
      elif i == '[':
         st.append(']')
      elif i == '(':
         st.append(')')
      else:
         if (len(st)<=0 or i != st.pop()):
            return False
   if len(st) != 0:
      return False
   return True

# st = input('Enter a set of bracket : ')
# print(st,f' is a valid one.') if isValid(st) else print(st,f' is an invalid one.')


'''
q4.) Perform binary substraction of 2 hexxdecimal inputs
  test1
   input : a = 4abe , b = 5a1    
   output:  17680  (19,121 - 1441)
'''
# a = int(input('Enter a hexdecimal number : '),16)
# b = int(input('Enter another hexdecimal number : '),16)

# res = a-b
# print('In decimal : ',res)
# print('\nIn binary form : ',bin(res))

def bitwiseOp(a,b):
   print(a,'AND',b,' = ',a&b)
   print(a,'OR',b,' = ',a|b)
   print(a,'XOR',b,' = ',a^b)
   print(a,' is right shift by ',b,' place = ',a>>b)
   print(a,' is left shift by ',b,' place = ',a<<b)
   print('negation of ',a,' : ',~a)
   print('negation of ',b,' : ',~b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

bitwiseOp(a,b)
