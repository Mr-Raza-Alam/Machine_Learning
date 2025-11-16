# num = input("Enter a number : ")

# try:
#   for i in range(1,4): 
#      print(f"{num}x{i} = {int(num) * i}")
# except ValueError as e:
#   print(f"There is some error {e}")

num = int(input("Enter a number: "))
results = [num * i for i in range(1, 11)]
result2 = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
print(results)
print(result2)
