# matrix

mA = [[row+col for col in range(1,4)] for row in range(1,4)]
mB = [[col-row for col in range(1,4)] for row in range(1,4)]

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

# or using list comphrension
mM = [
    [sum(mA[i][k]*mB[k][j] for k in range(3)) for j in range(3)]
    for i in range(3)
]

print(mM)