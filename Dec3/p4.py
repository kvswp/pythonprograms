#parent class

class Animal():

 def __init__(self):
  print("animal created")

 def who_am_i(self):
  print("i am animal")

 def eat(self):
  print("animal eating")

class Dog(Animal):

 def eat(self):
  print("dogs eating")

 def speak(self):
  print("bow bow")

anm = Animal()

anm.who_am_i()

dog1 = Dog()

dog1.eat()
dog1.speak()
