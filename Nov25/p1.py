def firstfun(name='someone'):
 '''
 its a function demo
 '''
 print("hello {}, you called function firstfun".format(name))

def add_func(n1,n2):
 return n1+n2

def even_check(num):
 return num%2 == 0

def check_even_lst(num_list):
 for n in num_list:
  if n%2 == 0:
#   print("{} is even".format(n))
   return True
  else:
   pass
 return False

def emp_check(work_hours):
 max_now = 0
 emp_of_month = ''
 for emp,hours in work_hours:
  if hours > max_now:
   max_now = hours
   emp_of_month = emp
  else:
   pass
 return(emp_of_month,max_now)


firstfun()
#firstfun("kvs")

sum = add_func(22,6)
print(sum)
sum1 = add_func('19','84')
print(sum1)

if even_check(10):
 print("not an odd no")

from random import randint 
mylist = [3,5,7,9,11]
for i in range(5):
 mylist.append(randint(11,90))
print(mylist)
if check_even_lst(mylist):
 print("even no there in list")	

timesheet = [('swp',32),('kv',40),('kota',24),('mrp',14)]
name,hours = emp_check(timesheet)
print("{} is the best emp and he worked for {} hours".format(name,hours))


