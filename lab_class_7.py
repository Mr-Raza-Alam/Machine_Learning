# Merging list
def printInp(arr):
    for ran in arr:
       print(ran[0],ran[1])

def helperMergeOv(arr):
    res = []
    res.append(arr[0])  # start with first interval
    for i in range(1, len(arr)):
        prev = res[-1]  # last added interval
        curr = arr[i]
        # if overlap: merge with previous
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            res.append(curr)
    return res

def mergeOverlap(n):
    arr = []
    print('Enter a set of ranges here : ')
    for i in range(n):
        empty = []
        j = 1
        while j <=2:
            empty.append(int(input()))
            j +=1
        arr.append(empty)
    print('Given Input : ')
    printInp(arr)
    # Main work is here
    print('\nOutput : ')
    print('The list of Non-overlapped ranges is \n',helperMergeOv(arr))

n = int(input('Enter required no. of line : '))
mergeOverlap(n)

      
    