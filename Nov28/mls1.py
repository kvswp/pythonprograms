from sys import exit
gameon = True
plst = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_game():
 print('\n'*100)
 print(" {} | {} | {} ".format(plst[0],plst[1],plst[2]))
 print("____________")
 print(" {} | {} | {} ".format(plst[3],plst[4],plst[5]))
 print("____________")
 print(" {} | {} | {} ".format(plst[6],plst[7],plst[8]))
 print("")


def position():
 choice = "sometext"
 accrange = list(range(1,10))
 print(accrange)
 withinrange = False

 while choice.isdigit() == False or withinrange == False:
  choice = input("player1/player2 - please select position from 1 to 9 - ")
  print(choice)
   
  if choice.isdigit():
   n = int(choice)
   if n in range(1,10):
    withinrange = True
   else:
    print("input is digit but not in correct range")
  else:
   print("not a digit, please correct it")

 return int(choice)

def update(val):
 if itr == 0 or itr%2 == 0: 
  plst[val-1] = p1
 else:
  plst[val-1] = p2 

def gameonchoice():
 print("do you want to continue - y  or n")
 p = input()
 if p == 'y':
  return True
 else:
  exit()

def checkwinner():
 if itr == 0 or itr%2 == 0:
  t = p1
  s = 'player1'
 else:
  t = p2
  s = 'player2'

 if (plst[0] ==  t and plst[1] == t and plst[2] == t) or (plst[0] ==  t and plst[3] == t and plst[6] == t) or (plst[0] ==  t and plst[4] == t and plst[8] == t) or (plst[2] ==  t and plst[4] == t and plst[6] == t) or (plst[2] ==  t and plst[5] == t and plst[8] == t) or (plst[1] ==  t and plst[4] == t and plst[7] == t) or (plst[3] ==  t and plst[4] == t and plst[5] == t) or (plst[6] ==  t and plst[7] == t and plst[8] == t):
  print("{} is winner".format(s))
  exit()
 else :
  pass
 if itr == 8:
  print("its a draw ")
  exit()

display_game()
itr = 0
p1 = input("player 1 plese select marker (x or o) ")
if p1 == 'x':
 p2 = 'o'
else:
 p2 = 'x'
print("p1 marker = " +p1)
print("p2 marker = " +p2)


while gameon:
 pn = position()
 update(pn)
 display_game()
 if itr > 3:
  checkwinner()
 itr += 1
 gameon = gameonchoice() 
