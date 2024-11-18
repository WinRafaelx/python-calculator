import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-12, -38), -50)

    def test_add_between_positive_negative(self):
        self.assertEqual(self.calc.add(-12, 31), 19)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(7, 1), 7)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_with_divisor_larger_than_dividend(self):
        self.assertEqual(self.calc.modulo(3, 10), 3)

if __name__ == '__main__':
    unittest.main()