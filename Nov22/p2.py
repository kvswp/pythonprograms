mylist = [1,2,3]
mylist_1 = ["swaroop",36,7.71]
l = len(mylist)
print("length of list1 = {}".format(l))
print("mylist[0] = {}".format(mylist[0]))
print("mylist_1[2] = {}".format(mylist_1[2]))
print("mylist_1[1:] = {}".format(mylist_1[1:]))

anothe_list = ["srm","mpccet",4123]
mylist_1 = mylist_1 + anothe_list
print("mylist_1 = {}".format(mylist_1))
mylist_1[0] = "venkat"
print("mylist_1 = {}".format(mylist_1))
mylist_1.pop()
print("mylist_1 = {}".format(mylist_1))
mylist_1.pop(2)
print("mylist_1 = {}".format(mylist_1))
mylist_1.append("Savitha")
print("mylist_1 = {}".format(mylist_1))

nlist = ['a','w','e','s','o','p','h']
numlist = [4,3,9,8,6]

print("nlist = {}".format(nlist))
print("numlist = {}".format(numlist))

nlist.sort()
numlist.sort()
print("nlist = {}".format(nlist))
print("numlist = {}".format(numlist))
numlist.reverse()
print("numlist = {}".format(numlist))
