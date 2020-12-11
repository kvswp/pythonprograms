class Line():
  
 def __init__(self,coor1,coor2):
  self.x1,self.y1 = coor1
  print(self.x1,self.y1)
  self.x2,self.y2 = coor2
  print(self.x2,self.y2)

 def distance(self):
  from math import sqrt
  d = sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
  print("distance = {}".format(d))

 def slope(self):
  s = (self.y2 - self.y1)/(self.x2 - self.x1)
  print("slope = {}".format(s))
 
 '''
 def __init__(self,coor1,coor2): 
  self.coor1 = coor1
  self.coor2 = coor2
  print(self.coor1,self.coor2)

 def slope(self):
  x1,y1 = self.coor1
  x2,y2 = self.coor2
  s = (y2 - y1)/(x2 - x1)
  print("slope = {}".format(s))

 def distance(self):
  x1,y1 = self.coor1
  x2,y2 = self.coor2
  from math import sqrt
  d = sqrt((x2-x1)**2 + (y2-y1)**2)
  print("distance = {}".format(d))
 '''
l1 = Line((2,3),(8,6)) 
l1.slope()
l1.distance()
