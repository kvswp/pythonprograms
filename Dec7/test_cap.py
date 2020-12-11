import unittest
import cap

class TestCap(unittest.TestCase):
 
 def testoneword(self):
  text = "python"
  result = cap.captext(text)
  self.assertEqual(result,"Python")

 def testtwoword(self):
  text = "kota venkat swaroop"
  result = cap.captext(text)
  self.assertEqual(result,"Kota Venkat Swaroop") 

if __name__ == '__main__':
 unittest.main()
