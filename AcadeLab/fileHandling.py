# import os
import csv
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

# line = 0
# data = True
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
# with open("AcadeLab/student.csv",'r') as f:
#     data = csv.reader(f)
#     # Access each row of data
#     i = 1
#     for row in data:
#         print(f"Row-{i} = {row}")
#         i +=1
#     print(f"Total no. of rows : {i-1}")

#Q.2
with open("AcadeLab/student.csv",'r') as f,open("AcadeLab/output.txt",'x',newline='') as fout:
    reader = csv.DictReader(f)
    data = list(reader)
    sorted_marks = sorted(data,key=lambda row:int(row['marks'] if row['marks'] != 'not a number' else 0),reverse=True)
    
    # Access each row of data
    count = 1
    total = 0
    writer = csv.writer(fout)
    for row in data:
       if row['marks'] !='not a number':
           total +=int(row['marks'])
       count +=1
    writer.writerow([f'Class Average = {round(total/count,2)}'])
    #
    writer.writerow(["Top-3"])
    for i in range(3):
        writer.writerow([sorted_marks[i]['name'],sorted_marks[i]['marks']])
    
    writer.writerow(["All students"])
   # 
    count = 0
    for row in sorted_marks:
        if row['marks'] != 'not a number':
            writer.writerow([row['name'],row['marks']])
        else:
            count +=1
    writer.writerow([f"Skipped rows : {count}"])


# with open("AcadeLab/student.csv",'r') as f:
#     reader = csv.DictReader(f)
#     data = list(reader)
#     sorted_data = sorted(data,key=lambda row:int(row['marks'] if row['marks'] != 'not a number' else 0),reverse=True)
    
    
# newRow = [{'name':'Ali','marks':89},{'name':'Bikarm','marks':79},]

# with open("AcadeLab/student.csv",'a',newline='') as fa:
#      fields = ['name','marks']    
#      writer = csv.DictWriter(fa,fieldnames=fields)
#      # now append new row
#      for row in newRow:
#          writer.writerow(row)


    
