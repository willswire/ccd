import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_shift(self):
        self.assertEqual(convertAndShift('0000000000001100'), 48)
        self.assertEqual(convertAndShift('0000000000001101'), 6)
        self.assertEqual(convertAndShift('0000000000000011'), 1)

    def test_ones_comp(self):
        self.assertEqual(convertAndShift('0100000000001100'), -65585)
        self.assertEqual(convertAndShift('0000000110001100'), -1585)
        self.assertEqual(convertAndShift('0000000000110010'), 200)
        self.assertEqual(convertAndShift('0000000000110100'), -209)
        self.assertEqual(convertAndShift('0000000110010011'), -202)

    
    def test_invalid_value(self):
        self.assertEqual(convertAndShift('0000020110010011'), 'INVALID_VALUE')
        self.assertEqual(convertAndShift('00000 0110010011'), 'INVALID_VALUE')
        self.assertEqual(convertAndShift('000000110010011 '), 'INVALID_VALUE')
        self.assertEqual(convertAndShift(' 000000110010011'), 'INVALID_VALUE')
    
    def test_invalid_length(self):
        self.assertEqual(convertAndShift('00000101100100111'), 'INVALID_LENGTH')
        self.assertEqual(convertAndShift('000001011001001'), 'INVALID_LENGTH')


if __name__ == '__main__':
    unittest.main()
