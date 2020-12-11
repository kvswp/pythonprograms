import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Eleven':11,'Twelve':12,'Thirteen':13,'Fourteen':14}

class Card:
 def __init__(self,suit,rank):
  self.suit = suit
  self.rank = rank
  self.value = values[rank]

 def __str__(self):
  return self.rank + " of " + self.suit

class Deck:
 def __init__(self):
  self.allcards = []
  for s in suits:
   for r in ranks:
    crd = Card(s,r)
    self.allcards.append(crd)

 def shuffle(self):
  random.shuffle(self.allcards)

 def dealone(self):
  return self.allcards.pop()

class Player:
 def __init__(self,name):
  self.name = name
  self.playercards = []

 def removeone(self):
  return self.playercards.pop(0)

 def addcards(self,newcard):
  if type(newcard) == type([]):
   self.playercards.extend(newcard)
  else:
   self.playercards.append(newcard)

 def __str__(self):
  return f"player {self.name} having {len(self.playercards)} cards"

player1 = Player("user")
player2 = Player("computer")

newdeck = Deck()
newdeck.shuffle()

for x in range(26):
 player1.addcards(newdeck.dealone())
 player2.addcards(newdeck.dealone())

gameon = True
count = 0

while gameon:
 count += 1
 print("count = {}".format(count))

 if len(player1.playercards) == 0:
  print("{} is winner".format(player2.name))
  gameon = False
  break

 if len(player2.playercards) == 0:
  print("{} is winner".format(player1.name))
  gameon = False
  break

 p1tmp = []
 p2tmp = []

 p1tmp.append(player1.removeone())
 p2tmp.append(player2.removeone())

 atwar = True
 while atwar:
  
  if p1tmp[-1].value > p2tmp[-1].value:
   player1.addcards(p1tmp)
   player1.addcards(p2tmp)
   atwar = False
  elif p2tmp[-1].value > p1tmp[-1].value:
   player2.addcards(p1tmp)
   player2.addcards(p2tmp)
   atwar = False
  else:
   print("WAR!")
   if len(player1.playercards) < 5:
    print("{} unable to go ahead in war".format(player1.name))
    print("{} WINS".format(player2.name))
    gameon = False
    break
   elif len(player2.playercards) < 5:
    print("{} unable to go ahead in war".format(player2.name))
    print("{} WINS".format(player1.name))
    gameon = False
    break
   else:
    for n in range(5):
     p1tmp.append(player1.removeone())
     p2tmp.append(player2.removeone())
     
      
