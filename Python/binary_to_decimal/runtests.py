import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):

    def test_binary_to_decimal_corner_cases(self):
        self.assertEqual("Invalid Input", binary_to_decimal(123))
        self.assertEqual("Invalid Input", binary_to_decimal(-10))
        self.assertEqual("Invalid Input", binary_to_decimal(200))
        self.assertEqual("Invalid Input", binary_to_decimal("123"))
        self.assertEqual(0, binary_to_decimal(000))

    def test_binary_to_decimal(self):
        self.assertEqual(8, binary_to_decimal(1000))
        self.assertEqual(13, binary_to_decimal(1101))
        self.assertEqual(19, binary_to_decimal(10011))
        self.assertEqual(25, binary_to_decimal(11001))


if __name__ == '__main__':
    unittest.main()
