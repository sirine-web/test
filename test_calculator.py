# tests/test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
    
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
    
    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
