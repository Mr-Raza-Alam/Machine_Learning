# first find no. of lines exit in the 2 files
# This will create a huge overhead b/c of multiple repeatition of opening files and apply operation 
lines1 = -1
data = True
with open("AcadeLab/demo.txt",'r') as f:
   while data :
      data = f.readline()
      lines1 +=1      

lines2 = -1
data = True
with open("AcadeLab/demo2.csv",'r') as f:
   while data :
      data = f.readline()
      lines2 +=1      

if (lines1 > lines2):
     with open("AcadeLab/merge.txt",'r+') as f:
        data1 = True
        data2 = True
        while data2:
         with open("AcadeLab/demo.txt",'r') as f1:           
           data1 = f1.readline()
           f.write(data1,"\n")
         with open("AcadeLab/demo2.csv",'r') as f2:
            data2 = f2.readline()
            f.write(data2,"\n")
     # now write remaining lines of file1
     with open("AcadeLab/demo.txt",'r') as f1:           
           while data1:
              data1 = f1.readline()
              f.write(data1,"\n")
elif (lines1 < lines2):
        with open("AcadeLab/merge.txt",'r+') as f:
          data1 = True
          data2 = True
          while data1:
             with open("AcadeLab/demo.txt",'r') as f1:           
                data1 = f1.readline()
                f.write(data1,"\n")
             with open("AcadeLab/demo2.csv",'r') as f2:
                data2 = f2.readline()
                f.write(data2,"\n")
         # now write remaining lines of file1
          with open("AcadeLab/demo2.csv",'r') as f2:           
           while data2:
              data2 = f2.readline()
              f.write(data2,"\n")
else :
      with open("AcadeLab/merge.txt",'r+') as f:
          data1 = True
          data2 = True
          while data1:
             with open("AcadeLab/demo.txt",'r') as f1:           
                data1 = f1.readline()
                f.write(data1,"\n")
             with open("AcadeLab/demo2.csv",'r') as f2:
                data2 = f2.readline()
                f.write(data2,"\n")
          f.write(f2.readline(),"\n")

    
         

        
