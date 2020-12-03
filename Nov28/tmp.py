lst1 = list(range(1,10))
print(lst1)

for i in range(1,10):
 n = int(input("please select a posion - "))
 print(n)
 lst1.pop(n-1)
 print(lst1)
