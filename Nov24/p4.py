from random import shuffle
from random import randint
mylist = list(range(1,11))
shuffle(mylist)
print(mylist)

num = randint(1,31)
print(num)

name = input("enter your name - ")
age = int(input('enter your age - '))
cgpa = float(input('enter your cgpa - '))

print("{}'s age is {} and he got {} cgpa in exams".format(name,age,cgpa))

n = age + 10
m = cgpa + 1.1
print(n,m)
