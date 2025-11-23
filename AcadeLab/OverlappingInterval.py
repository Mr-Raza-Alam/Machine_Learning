
def overlapp(lst):
     tmp = lst[0]
     r = 1
     while (r < len(lst)):
          if (tmp[1] > lst[r][0]): # means overlapping occurs
               lst[r-1][1] = lst[r][1]
               tmp = lst[r]
               lst.remove(lst[r])
               r -=1
          else:
               tmp = lst[r]
          r +=1
     print("\nAfter eliminating the overlap\n",lst)
lst = [
    [1,3],
    [2,6],
    [4,10],
    [9,40]]               
print("The original intervals : ",lst)
overlapp(lst)