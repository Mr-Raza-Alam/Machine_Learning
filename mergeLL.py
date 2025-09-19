# in-place Merge 2 linkedlists

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
    
    def display(self):
        curr = self.head

        while curr:
            print(curr.val,end='-->')
            curr = curr.next
        print('None')

def mergeLinkedList():
    l1 = LinkedList()
    l2 = LinkedList()
    
    # Add to list 1
    l1.addLast(4)
    l1.addLast(3)
    l1.addLast(5)
    l1.addLast(7)
    l1.addLast(8)
    l1.addLast(1)
   # Add to list2
    l2.addLast(6)
    l2.addLast(8)
    l2.addLast(9)
    l2.addLast(0)
    l2.addLast(2)
    l2.addLast(3)
   
    curr  = l1.head
    while curr.next is not None:
        curr = curr.next
    curr.next = l2.head
    print('After merging of 2 singly linkedlist ,new updated linkedlist is given below \n')
    l1.display()

mergeLinkedList()
