'''
Build a linklist data structure 
 add : first(), last() , middle()
 remove : first(), last() ,middle()
 reverselist()
 display() 
so ,here i am using Node class  and implementing True linkedlist 
'''
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def addFirst(self,x):
        if self.head is None:
            self.newNode = Node(x)
            self.head = self.newNode
        else:
            self.newNode = Node(x)
            self.newNode.next = self.head
            self.head = self.newNode
    def addLast(self,y):
        if self.head is None:
            self.newNode = Node(y)
            self.head = self.newNode
        else:
            self.newNode = Node(y)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = self.newNode
    def removeFirst(self):
        if self.head:
            self.head = self.head.next
    def removeLast(self):
        if self.head is None:
            return
        if self.head.next is None: # one Node
            self.head = None
            return
        curr = self.head
        while curr.next.next: # stop it before last node
            curr = curr.next
        curr.next = None

    def revList(self):
        if self.head is None:
            print("First add some node")
            return
        elif self.head.next is None:# only single node
            print(self.head.val,end="-->None")
            return     
        else:
            prev = None
            curr = self.head
            while curr:
                nxt = curr.next
                curr.next = prev # reverse
                # updation
                prev = curr
                curr = nxt 
            self.head = prev
    
    def display(self):
        curr = self.head

        while curr:
            print(curr.val,end='-->')
            curr = curr.next
        print('None')
        
    
ll = LinkedList()

print('Welcome to Linkedlist world.lets begin with its operation.')
print('press-1: to add at first'),print('press-2: to add at last')
print('press-3: to remove data at first'),print('press-4: to remove data at last')
print('press-5: to reverse the list'),print('press-6: to see the data of linkedlist.')

try:
    while True:
        opt = int(input('\nPress an option : '))
        match opt:
            case 1:
                x = int(input('Enter a data : '))
                ll.addFirst(x)
                print('Hurray!your data has been successfully added at first to the linkedlist.')
            case 2:
                x = int(input('Enter a data : '))
                ll.addLast(x)
                print('Hurray!your data has been successfully added at last to the linkedlist.')
            case 3:
                ll.removeFirst()
                print('Data has been removed at first.')
            case 4:
                ll.removeLast()
                print('Data has been removed at last.')
            case 5:
                ll.revList()
                print("The linkedlist has been reversed")
            case 6:
                print('The stored value in the linkedlist are \n')
                ll.display()
            case _:
                print('Invalid option.Try again')
                break
except ValueError as ve:
     print("Please press an option first!")