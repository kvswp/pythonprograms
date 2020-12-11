def askforint():

 while True:
  try:
   p = int(input("enter a no = "))
  except:
   print("not a valid number")
  else:
   print("p = {}".format(p))
   break
  finally:
   print("done...")

askforint()
