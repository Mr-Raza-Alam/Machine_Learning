# first find no. of lines exit in the 2 files

with open("AcadeLab/demo.txt",'r') as f1,open("AcadeLab/demo2.csv",'r') as f2,open("AcadeLab/merge.txt",'x') as fout:
       while True:
              line1 = f1.readline()
              line2 = f2.readline()

              if not line1 and not line2 : # if both files are done
                     break
              if line1:
                    fout.write(line1)
              if line2:
                    fout.write(line2)



