'''
objective : to find out and print the longest common subsequence among 2 given strings

input : st1 = 'ABCBDCAB' st2 = 'BDCABAC'
output : 'BDCAB'
'''
def lcs(st1,st2):
    res = ''
    if len(st1)>=len(st2):
        i,j= 0,0
        while(i<len(st1) and j <len(st2)):
            if(st1[i] == st2[j]):
                res +=st1[i] # or st[i]
                i +=1
                j +=1
            else :
                i +=1  
    else: # since len(st2) < len(st1)
        i,j= 0,0
        while(i<len(st1) and j <len(st2)):
            if(st1[i] == st2[j]):
                res +=st2[j] # or st[j]
                i +=1
                j +=1
            else:
                j +=1
    print('Longest Common Subsequence : ',res)

st1 = input('Enter a string : ')
st2 = input('Enter another string : ')
print('String-1 : ',st1,'\nString-2 : ',st2,'\n')
lcs(st1,st2)

        
