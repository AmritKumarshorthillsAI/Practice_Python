import unittest
import calc

class TestCalc(unittest.TestCase):

# all the test should start with the name test
    def test_add(self):
        result = calc.add(10, 5)
        # assert
        self.assertEqual(result, 15)

        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


    def test_subtract(self):
        
        # assert
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)


    def test_multiply(self):
        
        # assert
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    
    def test_divide(self):
        
        # assert
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        self.assertRaises(ValueError, calc.divide, 10, 0)

        # using context manager to handle valueError 
        with  self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()