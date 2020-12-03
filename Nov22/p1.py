
t = 2
print("hello world {}".format(t))
print("type(t) = {}".format(type(t)))
t = ["kota","venkat"]
print("hello world {}".format(t))
print(type(t))

s1 = 'swaroop'
s2 = "Venkat"
s3 = "i don't know"
print(s2,s1,s3)
#print("{} {} {}".format(s2,s1,s3))

mystring = "hello world"
print("mystring[0] = {}".format(mystring[0]))
print("mystring[6] = {}".format(mystring[6]))
print("mystring[7] = {}".format(mystring[7]))
print("mystring[-4] = {}".format(mystring[-4]))

print("mystring[2:] = {}".format(mystring[2:]))
print("mystring[:3] = {}".format(mystring[:3]))
print("mystring[2:5] = {}".format(mystring[2:5]))
print("mystring[::] = {}".format(mystring[::]))
print("mystring[::2] = {}".format(mystring[::2]))
print("mystring[0:7:3] = {}".format(mystring[0:7:3]))
print("mystring[::-1] = {}".format(mystring[::-1]))

name = "swaroop"
#name[0] = 'P'
oname = 'P' + name[1:]
print("{}".format(oname))
m = '2'
m = m * 10
print("{}".format(m))
x = "hello swaroop"
y = "sri rama raksha stotram"
print("{}".format(x.upper()))
print("{}".format(y.split()))
print("{}".format(y.split('a')))
print(f"my name is {name}")
