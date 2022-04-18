import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_gcd(self):
        amt, str = computeChange({'Q':3, 'D':7, 'P':14})
        self.assertEqual(1.59, amt)
        self.assertEqual('FRIES', str)
        amt, str = computeChange({'Q':3})
        self.assertEqual(.75, amt)
        self.assertEqual('NOTHING', str)
        amt, str = computeChange({'Q':3, 'D':7, 'N': 20, 'P':14})
        self.assertEqual(2.59, amt)
        self.assertEqual('BOTH', str)
        amt, str = computeChange({'H':0, 'Q':3, 'D':7, 'N':20, 'P':14})
        self.assertEqual(2.59, amt)
        self.assertEqual('BOTH', str)
        amt = computeChange({'Q':3, 'D':7, 'N': -2, 'P':14})
        self.assertEqual(0, amt)
        amt, str = computeChange({'Q':2, 'D':0, 'N': 10, 'P':0})
        self.assertEqual(1.00, amt)
        self.assertEqual('SODA', str)


if __name__ == '__main__':
    unittest.main()
