'''
build a queue(FIFO) data structure in python

properties of python are :
  enque() means add(x)
  deque() means remove() data from first entry
  peek() means return first entry value
  isEmpty() means check whether the queue is empty  or not
'''

class Queue:
    def __init__(self):
        self.lst = []
    def enque(self,x):
        self.lst.append(x)
    def deque(self):
         self.lst.pop(0) if self.isEmpty() == False else print("Queue is empty")
    def peek(self):
        return self.lst[0]
    def isEmpty(self):
        return len(self.lst) == 0
    def display(self):
        for i in self.lst:
            print(i,end=' ')
    
q = Queue() 

n = int(input('Enter no. of data entry for sample : '))
print('\nOk add',n,' data to the respective queue')
for i in range(1,n+1):
    q.enque(int(input(f'Enter entry-{i} : ')))

print('\nNow you can start queue operation game\nlets begin ')
print('press-1: to enque new data');print('press-2: to deque a data');print('press-3: to peek first data');print('press-4: to check whether the queue is empty or not')
print('press-5: to see the data.')

while True:
    opt = int(input('\nPress an option : '))
    match opt:
        case 1:
            print('You want to add data.Good')
            print('Press- O: to add single data.'),print('Press- M: to add multiple data.')
            choose = input('O or M ?? : ')
            if choose == 'O':
                y = int(input('Enter your required data : '))
                q.enque(y)
            elif choose == 'M':
                n = int(input('Enter a no. required to add the data : '))
                for i in range(1,n+1):
                    q.enque(int(input()))
            else:
                print('Please select a correct option.')
            # print('Hurray!your data has been successfully added to the queue.')
        case 2:
            print('Do you really delete a data?hit 1,if yes otherwise hit 0')
            q.deque() if int(input()) == 1 else None
        case 3:
            print('The peek value of the queue = ',q.peek())
        case 4: 
            print('Yes,queue is empty.') if q.isEmpty() else print('No,queue is unempty.')
        case 5:
            print('Here is your data stored in a queue.')
            q.display()
        case _:
            print('Invalid option.Try again')
            break
    


    
