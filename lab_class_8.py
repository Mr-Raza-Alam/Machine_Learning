#  longest subtring without repeating characters
   
def LSC(st):
    s = ''
    l = 0
    for i in st:
        if i in s:
            s = s[s.index(i)+1:] # slicing of 
        else:
           s += i
           l = max(l,len(s))


    return l

st = input('Enter a string : ')
print('The longest substring without repeating characters is : ',LSC(st))
