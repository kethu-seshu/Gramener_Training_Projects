import unittest
import calc

class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        # self.assertEqual(calc.add(0, 0), 1) # error
        
        
    def test_sub(self):
        self.assertEqual(calc.subtract(3, 2), 1)
        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.subtract(-3, 2), -5)
        self.assertEqual(calc.subtract(3, -2), 5)    
        # self.assertEqual(calc.subtract(0, 1), 1)  # error
        
        
    def test_divide(self):
        self.assertEqual(calc.divide(4, 2), 2)
        self.assertEqual(calc.divide(1, 2), 0.5)
        self.assertEqual(calc.divide(-1, 2), -0.5)
        self.assertEqual(calc.divide(1, -2),-0.5 )
        self.assertEqual(calc.divide(0, 1),0 )
        # self.assertEqual(calc.divide(1, 0),0 )   # ZeroDivisionError
        # self.assertEqual(calc.divide(0, 1),1 ) # error
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 2), 6)
        self.assertEqual(calc.multiply(3, -2), -6)
        self.assertEqual(calc.multiply(-3, 2), -6)
        self.assertEqual(calc.multiply(3, 0), 0)
        self.assertEqual(calc.multiply(0, 2), 0)
        

if __name__== "__main__":
    unittest.main()