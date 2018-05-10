import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
    
    def test_add(self):
        self.calculator.push(1)
        self.calculator.push(1)
        self.calculator.push('+')
        self.assertEqual(2, self.calculator.pop())
    
    def test_sub(self):
        self.calculator.push(1)
        self.calculator.push(1)
        self.calculator.push('-')
        self.assertEqual(0, self.calculator.pop())

    def test_mul(self):
        self.calculator.push(1)
        self.calculator.push(2)
        self.calculator.push('*')
        self.assertEqual(2, self.calculator.pop())
    
    def test_div(self):
        self.calculator.push(2)
        self.calculator.push(2)
        self.calculator.push('/')
        self.assertEqual(1, self.calculator.pop())


if __name__ == '__main__':
    unittest.main()
