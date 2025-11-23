# Product of Array Except Self 
# Constraint - O(n),no division
class NegativeValueError(Exception):
    pass

try:

    n = int(input("Enter the array's size : "))  
    if n<0:
        raise NegativeValueError("Size cannot be negative.!")
    num = []
    for i in range(n):
        num.append(int(input(f"Enter element-{i+1} : ")))

    print(f"The input : {num}")

    # Apply logic 
    prefix = [1]
    t = 1
    for i in range(1,n):
        t *=num[i-1]
        prefix.append(t)

    suffix = [1]
    t = 1
    num = num[::-1] # reverse the original list
    for i in range(1,n):
        t *=num[i-1]
        suffix.append(t)

    suffix = suffix[::-1] # reverse the suffix list
    t = 0
    for ele in suffix:
        prefix[t] = prefix[t]*ele
        t +=1
    print(f"The output : {prefix}")
except ValueError as ve:

    print(f"Element is vacant.fill up it")
except NegativeValueError as ne:
    print(ne)

    



