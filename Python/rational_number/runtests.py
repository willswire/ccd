import unittest
from testfile import *


class RationalNumberTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaultRational = RationalNumber()
        cls.rational1 = RationalNumber(24, 36)
        cls.rational2 = RationalNumber(11, 55)

    def test_printFraction(self):
        self.assertEqual("0/1", self.defaultRational.printFraction())
        self.assertEqual("2/3", self.rational1.printFraction())
        self.assertEqual("1/5", self.rational2.printFraction())

    def test_printDecimal(self):
        self.assertEqual(0.00, self.defaultRational.printDecimal())
        self.assertEqual(0.67, self.rational1.printDecimal())
        self.assertEqual(0.20, self.rational2.printDecimal())

    def test_add(self):
        self.assertEqual("13/15", self.rational1.add(self.rational2).printFraction())
        self.assertEqual(0.87, self.rational1.add(self.rational2).printDecimal())
        self.assertEqual("4/3", self.rational1.add(self.rational1).printFraction())
        self.assertEqual(1.33, self.rational1.add(self.rational1).printDecimal())
        self.assertEqual("2/5", self.rational2.add(self.rational2).printFraction())
        self.assertEqual(0.40, self.rational2.add(self.rational2).printDecimal())

    def test_subtract(self):
        self.assertEqual("7/15", self.rational1.subtract(self.rational2).printFraction())
        self.assertEqual(0.47, self.rational1.subtract(self.rational2).printDecimal())
        self.assertEqual("0/1", self.rational1.subtract(self.rational1).printFraction())
        self.assertEqual(0.00, self.rational1.subtract(self.rational1).printDecimal())
        self.assertEqual("0/1", self.rational2.subtract(self.rational2).printFraction())
        self.assertEqual(0.00, self.rational2.subtract(self.rational2).printDecimal())

    def test_multiply(self):  
        self.assertEqual("2/15", self.rational1.multiply(self.rational2).printFraction())
        self.assertEqual(0.13, self.rational1.multiply(self.rational2).printDecimal())
        self.assertEqual("4/9", self.rational1.multiply(self.rational1).printFraction())
        self.assertEqual(0.44, self.rational1.multiply(self.rational1).printDecimal())
        self.assertEqual("1/25", self.rational2.multiply(self.rational2).printFraction())
        self.assertEqual(0.04, self.rational2.multiply(self.rational2).printDecimal())

    def test_divide(self):
        self.assertEqual("1/1", self.rational1.divide(self.rational1).printFraction())
        self.assertEqual(1.00, self.rational1.divide(self.rational1).printDecimal())
        self.assertEqual("10/3", self.rational1.divide(self.rational2).printFraction())
        self.assertEqual(3.33, self.rational1.divide(self.rational2).printDecimal())
        self.assertEqual("1/1", self.rational2.divide(self.rational2).printFraction())
        self.assertEqual(1.00, self.rational2.divide(self.rational2).printDecimal())

        try:
            RationalNumber(24, 0)
        except Exception as error:
            self.assertEqual("Cannot divide by zero", str(error))


if __name__ == '__main__':
    unittest.main()
