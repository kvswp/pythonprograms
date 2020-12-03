
'''
def myfunc(a,b,c,d,e=0):
 return(a+b+c+d+e)

n = myfunc(10,10,10,10,10,10,20)
print(n)
'''
def myfunc(*arg):
 sum = 0
 for n in arg:
  sum = sum + n
 print(sum) 

myfunc(1,2)
myfunc(1,3,5)
myfunc(2,5,9,10,12)

def myfun(*args,**kwargs):
 if 'fruit' in kwargs:
  print("{} & {} is for you".format(args[0],kwargs['food']))
 else:
  pass

myfun(10,20,30,fruit = 'orange',food = 'eggs',animal = 'dog') 

