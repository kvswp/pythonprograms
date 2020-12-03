x = 1
while x < 5:
 if x == 3:
  break
 print("x = {}".format(x))
 x += 1
 
for num in range(0,5): 
 if num == 2:
  continue   
 print("num = {}".format(num))

'''
index_count = 0
mys = "swaroop"
for l in mys:
#print("at index {} mys - {}".format(index_count,l))
 print(mys[index_count])
 index_count += 1
'''

mys = "kvswaroop"
for item in enumerate(mys):
 print(item)

for index,letter in enumerate(mys):
 print(index)
 print(letter)

for num in range(2,11,2):
 print(num)

myl1 = [1,2,3,4,5]
myl2 = ['a','b','c']
myl3 = [100,200,300,400]

newl = zip(myl1,myl2,myl3)
print(newl)

for a,b,c in zip(myl1,myl2,myl3):
 print(b)

rndl = [['p','u','l'],['m','j','n'],['r','k','y'],['s','t','d']]
for lst in rndl:
 x = lst
 if 'p' in x:
  print("Ps ready to mingle")
 elif 'k' not in x:
  pass
 else:
  print("Kotas arrived - standing ovation please")
