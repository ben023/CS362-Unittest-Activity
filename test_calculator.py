import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator.multiply(2,2), 4)
    def test2(self):
        self.assertEqual(calculator.divide(2,0), "Error")
    def test3(self):
        self.assertEqual(calculator.add(2,3), 5)
    def test4(self):
        self.assertEqual(calculator.subtract(3,2), 1)


if __name__ == '__main__':
    unittest.main()