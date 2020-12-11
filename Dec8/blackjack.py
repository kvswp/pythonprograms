import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'King':10,'Queen':10,'Ace':11}

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

 def __str__(self):
  deck_comp = ' '
  for card in self.allcards:
   deck_comp += '\n ' +card.__str__() 
  return 'The deck has:' + deck_comp

 def shuffle(self):
  random.shuffle(self.allcards)

 def dealone(self):
  singlecard = self.allcards.pop()
  return(singlecard)

class Hand:
 def __init__(self,name):
  self.name = name
  self.cards = []
  self.value = 0
  self.aces = 0

 def addcards(self,card):
  self.cards.append(card)
  self.value += values[card.rank]
  if card.rank == 'Ace':
   self.aces += 1

 def adjustforace(self):
  while self.value > 21 and self.aces > 0:
   self.value -= 10
   self.aces -= 1

class Chips:
 def __init__(self,total=100):
  self.total = total
  self.bet = 0

 def winbet(self):
  self.total += self.bet

 def losebet(self):
  self.total -= self.bet

def showcards(hndobj):
 if hndobj.name != "Dealer":
  print("player 1 cards - ")
  n = len(hndobj.cards)
  for itm in range(n):
   print(hndobj.cards[itm])
 else:
  print("dealer open card - ")
  print(hndobj.cards[0])

def mybet(cobj):
 while True:
  try:
   cobj.bet = int(input("please enter your bet - "))
  except:
   print("wrong input, please enter correctly")
  else:
   if cobj.bet > cobj.total:
    print("bet is greater than available chips {}".format(cobj.total))
   else:
    print("bet amount is - {}".format(cobj.bet))
    break
 
d1 = Deck()
d1.shuffle()
print(len(d1.allcards))

h1 = Hand("Player1")
h2 = Hand("Dealer")

for itm in range(2):
 h1.addcards(d1.allcards.pop())
 h2.addcards(d1.allcards.pop())

showcards(h1)
showcards(h2)
