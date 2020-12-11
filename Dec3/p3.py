
class Circle():

 pi = 3.14
 
 def __init__(self,radius):
  self.radius = radius
  self.area =  Circle.pi * radius**2

 def get_circumference(self):
  return 2 * self.radius * Circle.pi

mycircle = Circle(10)

print(mycircle.pi)
print(mycircle.radius)
print(mycircle.area)

f = mycircle.get_circumference()
print(f)

