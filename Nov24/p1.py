orglist = [["swar",32,8,'O'],["vandita",25,9,'O'],["satish",35,7.5,'R'],["swaroop",36,7.71,'O']]
mylist = []

for lst in orglist:
#print(lst)
 mylist = lst
 if mylist[0] == 'swaroop':
  print("hold on {}, we will get back to you".format(mylist[0]))
 elif mylist[2] >= 7 and (mylist[3]=='R' or mylist[1] < 30):
  print("eligible for next level Mr/Miss {}".format(mylist[0]))
 else:
  print("look for other oppurtunities Mr/Miss {}".format(mylist[0]))



