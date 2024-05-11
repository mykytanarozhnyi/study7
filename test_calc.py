import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def test_of_test(self):
        self.assertTrue(True)
    def test_add(self):
        result = Calc.add(2,2)
        self.assertEqual(result, 15)

    def test_sub(self):
        result = Calc.sub(10,5)
        self.assertEqual(result,15)
    def test_mult(self):
        result = Calc.mult(10,5)
        self.assertEqual(result,5)
    def test_leveling(self):
        result = Calc.leveling(5,2)
        self.assertEqual(result,10)
    def test_division(self):
        result = Calc.division(2,2)
        self.assertEqual(result,0.5)
    def test_intdiv(self):
        result = Calc.intdiv(15,5)
        self.assertEqual(result,3)
    def test_remofdiv(self):
        result = Calc.intdiv(25,4)
        self.assertEqual(result,3)






if __name__ == '__main__':
    unittest.main()

