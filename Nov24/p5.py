mystring = 'hello'
'''
mylist = []
for let in mystring:
 mylist.append(let)
print(mylist)
LIST COMPREHENSION
'''

mylist = [let for let in mystring]
print(mylist)

myl1 = [x for x in 'sachin']
print(myl1)

myl2 = [num for num in range(1,11)]
print(myl2)

myl3 = [x**2 for x in range(0,10) if x%2 == 0]
print(myl3)

cel = [12,20,24,32,40.5]

far = [(9/5*temp+32) for temp in cel]
print(far)

result = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(result)

'''
myls = []
for x in [2,4,6]:
 for y in [100,200,400]:
  myls.append(x*y)
print(myls)
'''

mls = [x*y for x in [2,4,6] for y in [10,100,1000]]
print(mls)
