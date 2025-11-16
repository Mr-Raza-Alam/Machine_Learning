import os
# try:

#     f = open("AcadeLab/demo.txt","r")
#     # now apply operation on file f
#     # read the data from the file f
#     data = f.read()
#     print("The file's data\n",data)
#     # As a active and smart developer,after completing the desire operations on the open file ,we must close it for security purpose
#     f.close()
# except FileNotFoundError as e:
#     print(e,"\nCorrect the file path")
# except SyntaxError as se :
#     print(se,"\nMake sure ,you using correct syntax")

# write operation using with syntax
# with open("AcadeLab/demo2.csv",'r+') as f:
#     print(f.read(10))
#     print(f.readline())
#     f.seek(f.tell())
#     n = f.write("Pea")
#     print(f.read())
#     print("No. of character write new data = ",n)

# Now we find no. of lines exits in a file in 'a+' mode 

line = 0
data = True
# with open("AcadeLab/demo.txt",'r') as f:
#    while data:
#       data = f.readline()
#       line +=1
# print("The no. of lines in the file = ",line-1)# -1 b/c it count 1 extra empty line i.e empty string that is EOF

# with open("AcadeLab/demo2.csv",'r+') as f:
#         while data:
#            data = f.readline()
#            line +=1
#         print("The no. of lines in the file = ",line-1)

# os.remove("AcadeLab/Sample.txt")  # it deleted the given file from the system 
