ml = [('swp',84),('ujju',81),('padma',63),('suri',53)]
mls = []
mlyob = []

#Tuple unpacking
for a,b in ml:
 mls.append(a)
 mlyob.append(b)

print("mls = {}".format(mls))
print("mlyob = {}".format(mlyob))
print("\n")
kl = [('sss',71,35,97),('www',92,67,85),('aaa',66,77,81),('rrrr',62,45,90),('ooo',55,67,78)]
l13 = []

for a,b,c,d in kl:
 print(a,b,c,d) 
 l13.append(b+d)

print("max in l13 = {}".format(max(l13)))
count = 0

for ls in l13:
 if max(l13) == ls:
  break
 count += 1

print("{} is the topper this year".format(kl[count][0]))

print("\n")

d = {'k1':'bvv','k2':'sachdeva','k3':'mpccet','k4':'srm','k5':'ceeri','k6':'tesi','k7':'kpit','k8':'qualcomm'}

for k,v in d.items():
 print(v)
