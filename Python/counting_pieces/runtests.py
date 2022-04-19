import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_count_pieces_corner_cases(self):
        self.assertEqual([0, 0, 0, 0], count_pieces(""))
        self.assertEqual([0, 0, 1, 0], count_pieces(" "))
        self.assertEqual([4, 0, 3, 4], count_pieces("1 2 3 4"))
        self.assertEqual([0, 4, 2, 1], count_pieces(" word "))

    def test_count_pieces(self):
        self.assertEqual([1, 13, 3, 4], count_pieces("We have 8 digits."))
        self.assertEqual([1, 13, 5, 4], count_pieces(" We have 8 digits ."))
        self.assertEqual([2, 35, 9, 10], count_pieces("I worked at IPSecure for 2 years and 3 months."))
        self.assertEqual([2, 43, 10, 11], count_pieces("Eight quick foxes jumped over 8 fences and 8 lazy dogs."))


if __name__ == '__main__':
    unittest.main()
