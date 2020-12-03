from random import shuffle

def shuflist(plist):
 shuffle(plist)
 return(plist)

def pguess():
 guess = 9 
 while guess not in [0,1,2]:
  guess = int(input("pick a no - 0,1 or 2\n"))
  print(guess)
 return (guess)

def check_guess(plist,guess):
 if plist[guess] == 'o':
  print("correct")
 else:
  print("wrong guess")
  print(plist)


mylist = ['o','','']
lst_aft_shuf =  shuflist(mylist)
g = pguess()
check_guess(lst_aft_shuf,g) 
