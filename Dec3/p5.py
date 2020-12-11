
class Dog():

 def __init__(self,name):
  self.name = name

 def speak(self):
  print("{} - bow bow".format(self.name))

class Cat():

 def __init__(self,name):
  self.name = name

 def speak(self):
  print("{} - meow meow".format(self.name))

d1 = Dog("dockey")

c1 = Cat("tom")

d1.speak()
c1.speak()

for p in [d1,c1]:
 print(type(p))
 p.speak()
