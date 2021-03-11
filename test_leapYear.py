import unittest
import leapYear

class testLeapYear(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapYear.leapYear(2),"It is not a leap year.")
    def test2(self):
        self.assertEqual(leapYear.leapYear(400), "It is a leap year.")
if __name__ == '__main__':
    unittest.main()