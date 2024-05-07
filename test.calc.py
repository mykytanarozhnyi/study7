import unittest
import calc
class TestCalc(unittest.TestCase):

    def test_of_test(self):
        self.assertTrue(True)
    def test_add(self):
        result = calc.add(2,2)
    def test_sub(self):
        result = calc.sub(10,5)
        self.assertEqual(result, 5)

    def test_sub(self):
        result = calc.sub(5,10)
        self.assertEqual(result, -5)


if __name__ == '__main__':
    unittest.main()

