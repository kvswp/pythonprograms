class Dog():

 species = 'mammal'

 def __init__(self,breed,name,spots):
  self.breed = breed
  self.name = name
  self.spots = spots
 
 def bark(self,var):
  print("{} please be calm {} is here".format(self.name,var))

#mydog = Dog(breed = 'desi',name = 'dockey',spots = False)
mydog = Dog('pomerian','lily',True)
print(mydog)
print(mydog.breed,mydog.name,mydog.species)

if mydog.spots:
 print("get some one without spots")
else:
 print("we can proceed") 

mydog.bark("doctor")
