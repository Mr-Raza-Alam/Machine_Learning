'''
build a stack(LIFO) data structure in python

properties of python are :
  Push() means add(x)
  Pop() means remove() data from first entry
  peek() means return first entry value
  isEmpty() means check whether the queue is empty  or not
'''

class Stack:
    def __init__(self):
        self.lst = []
    def Push(self,x):
        self.lst.append(x)
    def Pop(self):
         self.lst.pop() if self.isEmpty() == False else print("Queue is empty")
    def peek(self):
        return self.lst[-1]
    def isEmpty(self):
        return len(self.lst) == 0
    def display(self):
        for i in reversed(self.lst): # Remember reversed() a method used to reverse the list element and return a list
            print(i,end=' ')

st = Stack() 

n = int(input('Enter no. of data entry for sample : '))
print('\nOk add',n,'data to the respective stack.')
for i in range(1,n+1):
    st.Push(int(input(f'Enter entry-{i} : ')))

print('\nNow you can start stack  operation game\nlets begin ')
print('press-1: to push new data');print('press-2: to pop a data');print('press-3: to peek top data');print('press-4: to check whether the queue is empty or not')
print('press-5: to see the data.')

while True:
    opt = int(input('\nPress an option : '))
    match opt:
        case 1:
            print('You want to add data. Good!\n')
            print('Press- O: to add single data.'),print('Press- M: to add multiple data.')
            choose = input('O or M ?? : ')
            if choose == 'O':
                y = int(input('Enter your required data : '))
                st.Push(y)
            elif choose == 'M':
                n = int(input('Enter a no. required to add the data : '))
                for i in range(1,n+1):
                    st.Push(int(input()))
            else:
                print('Please select a correct option.')
            # print('Hurray!your data has been successfully added to the queue.')
        case 2:
            print('Do you really delete a data?hit 1,if yes otherwise hit 0')
            st.Pop() if int(input()) == 1 else None
        case 3:
            print('The peek value of the queue = ',st.peek())
        case 4: 
            print('Yes,stack is empty.') if st.isEmpty() else print('No,stack is unempty.')
        case 5:
            print('Here is your data stored in a stack.')
            st.display()
        case _:
            print('Invalid option.Try again')
            break
    