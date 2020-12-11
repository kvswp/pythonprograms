class Account():

 def __init__(self,owner,balance):
  self.owner = owner
  self.balance = balance

 def __str__(self):
  return f"owner = {self.owner}\nbalance = {self.balance}"

 def deposit(self,amount):
  self.balance += amount
  print("{} deposited, total available balance = {}".format(amount,self.balance)) 

 def withdraw(self,amount):
  if amount < self.balance:
   self.balance -= amount
   print("{} withadrawn, total available balance = {}".format(amount,self.balance))
  else:
   print("Your account has not enough balance to withdraw {}".format(amount))
   print("available balance = {}".format(self.balance))  

a1 = Account("swp",1000)
print(a1)
a1.deposit(200)
a1.withdraw(500)
a1.withdraw(5000)
