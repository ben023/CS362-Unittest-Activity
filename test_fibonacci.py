import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test1(self):
        self.assertEqual(fibonacci.fib(1), 1)
    def test2(self):
        self.assertEqual(fibonacci.fib(2), 1)
    def test3(self):
        self.assertEqual(fibonacci.fib(3), 2)
    def test4(self):
        self.assertEqual(fibonacci.fib(4), 3)

    def test5(self):
        self.assertEqual(fibonacci.fib(0), 0)

    def test6(self):
        self.assertEqual(fibonacci.factorial(2), 2)

    def test7(self):
        self.assertEqual(fibonacci.factorial(4), 24)

    
# pytest cases:
def test_fib():
    assert fibonacci.fib(1) == 1
    assert fibonacci.fib(3) == 2 

if __name__ == '__main__':
    unittest.main()


