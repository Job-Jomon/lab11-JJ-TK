import unittest
import math
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    logarithm,
    exponent,
    square_root,
    hypotenuse,
)

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 5), 6)
        self.assertEqual(add(1253, 1450), 2703)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2,1),1)
        self.assertEqual(subtract(264,54),210)
        self.assertEqual(subtract(14,16),-2)



    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        # Note: divide(a, b) calculates b / a
        self.assertEqual(divide(2, 6), 3.0)
        self.assertEqual(divide(4, -12), -3.0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0,54)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(5, 125), 3)
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 34)
    
    def test_log_invalid_argument(self):
        # Base <= 0, base == 1, or value <= 0 should raise ValueError
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        # Hypotenuse should handle negative numbers correctly
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()