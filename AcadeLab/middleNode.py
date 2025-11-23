# Find middle node in a single pass

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

def middleNode(l):
    s = l.head # slow pointer it travels 1step at a time
    f = s  # fast pointer ---> it travels 2step at a time    
    while f is not None and f.next is not None:
        s = s.next
        f = f.next.next
    # when f will be at end of list then s will be at middle of list
    return s  

def find_middle(start, end):
    slow = fast = start
    while fast != end and fast.next != end:
        slow = slow.next
        fast = fast.next.next
    return slow

def binary_search_linked_list(head, target):
    start = head
    end = None
    while start != end:
        mid = find_middle(start, end)
        if mid.val == target:
            return True
        elif mid.val < target:
            start = mid.next
        else:
            end = mid
    return False

l = LinkedList()
# Add
l.addLast(2)
l.addLast(5)
l.addLast(3)
l.addLast(7)
l.addLast(4)
print('The middle node value of linkedlist is ',middleNode(l).val)

