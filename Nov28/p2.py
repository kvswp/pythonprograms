#LEGB Rule

x = 50

def func(x):
# global x 
 print("x = {}".format(x))
 x = 200
 print("x = {}".format(x))
 return x


print("x = {}".format(x))
x = func(x)
print("x = {}".format(x))
