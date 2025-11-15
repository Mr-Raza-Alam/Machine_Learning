'''
Build a linklist data structure 
 add : first(), last() , middle()
 remove : first(), last() ,middle()
 reverselist()
 display() 
so ,here i am using list  and implementing linkedlist normally 
'''
class Linkedlist:
    def __init__(self):
        self.lst = []
    def addFirst(self,x):
        if self.isEmpty():
           self.lst.append(x)
        else:         
            self.lst.insert(0,x)
    def addLast(self,x):
        self.lst.append(x)
    def addMiddle(self,idx,x):
        self.lst.insert(idx,x)
    def removeFirst(self):
        self.lst.pop(0)
    def removeLast(self):
        self.lst.pop()
    def removeMiddle(self,idx):
        self.lst.pop(idx)        
    def isEmpty(self):
        return len(self.lst) == 0
    def reverse_ll(self):
        # self.lst = self.lst[::-1]  # inefficient w.r.t memory
        i,j= 0,len(self.lst)-1
        while i<=j:
            self.lst[i],self.lst[j] = self.lst[j],self.lst[i]
            i +=1
            j -=1
            
    def display(self):
        for i in self.lst:
            print(i,end='-->')
    
ll = Linkedlist() 

print('Welcome to Linkedlist world.lets begin with its operation.')
print('press-1: to add')
print('\t  Press- F: to add data at first.'),print('\t  Press- L: to add data at last.'),print('\t  Press- M: to add data at middle.')

print('press-2: to remove'),print('press-3: to reverse the list item')
print('press-4: to see the data.')

while True:
    opt = int(input('\nPress an option : '))
    match opt:
        case 1:
            print('You want to add data. Good!\n')
            choose = input('F or M or L ?? : ')
            if choose == 'F':
                y = int(input('Enter your required data : '))
                ll.addFirst(y)
            elif choose == 'L':
                y = int(input('Enter your required data : '))
                ll.addLast(y)
            elif choose == 'M':
                i = int(input('Enter the position to add a data : '))
                n = int(input('Enter your required data : '))
                ll.addMiddle(i,n)
            else:
                print('Please select a correct option.')
            # print('Hurray!your data has been successfully added to the queue.')
        case 2:
            print('Ok you want to delete data.\n')
            choose = input('f or f or m ?? : ') 
            if choose == 'f':
                ll.removeFirst()
            elif choose == 'l':
                ll.removeLast()
            elif choose == 'M':
                i = int(input('Enter the position to delete a data : '))
                ll.removeMiddle(i)
            else:
                print('Please select a correct option.')       
        case 3:
            print('After reversing linked list,we have \n')
            ll.reverse_ll()
        case 4:
            print('Here is your data stored in a stack.')
            ll.display()
        case _:
            print('Invalid option.Try again')
            break
    