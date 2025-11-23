# matrix
rowA,colA = int(input("Enter no. of rows of matrix A : ")),int(input("Enter no. of cols of matrix A : "))
rowB,colB = int(input("Enter no. of rows of matrix B : ")),int(input("Enter no. of cols of matrix B : "))
# Design the matrix
mA = [[row+col for col in range(1,colA+1)] for row in range(1,rowA+1)]
mB = [[col-row for col in range(1,colB+1)] for row in range(1,rowB+1)]

# or using list comphrension
try:
    print("matrix A : ",mA)
    print("\nmatrix B : ",mB)

    if colA != rowB :
        print("Matrice cann't be multiply,\nB/c, no. of colsA is unequal to no. of rowsB")
    else:
        mM = [
            [sum(mA[i][k]*mB[k][j] for k in range(colA)) for j in range(colB)]
            for i in range(rowA)
        ]
        print("\nmatrix(A x B) : ",mM)
except IndexError as ie:
    print(ie)

# using brute force approach ,implement matrix multiplication
# mM = []
# for i in range(3):
#     curr = []
#     for j in range(3):
#         sum = 0
#         for k in range(3):
#             sum += mA[i][k]*mB[k][j]
#         curr.append(sum)
#     mM.append(curr)