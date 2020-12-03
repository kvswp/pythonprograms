myfile = open("myinfo.txt")
print("{}".format(myfile.read()))
myfile.seek(0)
#print("{}".format(myfile.readlines()))
mylist = myfile.readlines()
print("mylist = {}".format(mylist))
myfile.close()

cf = open("/home/admin1/cpp/p1.cpp")
str = cf.read()
print(str)

with open ('inf.txt',mode='w+') as m1:
 m1.write("i am good boy")
 m1.seek(0)
 content = m1.read()
 print(content)
