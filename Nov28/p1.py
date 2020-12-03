def square(num):
 return num**2

def evencheck(num):
 return num%2 == 0

mynums = [1,2,3,4,5,6]
#r = []

#for n in mynums:
# r.append(square(n))

#print(r)

#for item in map(square,mynums):
# print(item)

#for item in filter(evencheck,mynums):
# print(item) 

nlst = list(map(square,mynums))
print(nlst)

nlst1 = list(filter(evencheck,mynums))
print(nlst1)

from random import randint
 
tlst = [21,22,23,24,25,26,27,28,29,30]
no = randint(1,5)
print(no)
wlst = list(filter(lambda num: num%no == 0,tlst))
print(wlst) 

age = [10,36,7,67,44,22,14,19,40]

adults = list(filter(lambda n:n>18,age))
print(adults)

names = ["swaroop","savitha","ujju","leelamohan","sharat","suri","padma"]

#uppernames = list(map(str.upper ,names))
uppernames = list(map(lambda n:n.upper(),names))
print(uppernames) 

