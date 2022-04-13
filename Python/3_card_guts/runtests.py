import unittest
from testfile import *

class CheckRideTestOne(unittest.TestCase):
    def test_3_kind(self):
        self.assertEqual([3,3,3], findGutsWinner([14,14,10], [3,3,3]))
        self.assertEqual([3,3,3], findGutsWinner([2,2,2], [3,3,3]))
        self.assertEqual([3,3,3], findGutsWinner([3,3,3], [2,2,2]))
    
    def test_pair(self):
        self.assertEqual([2,2,10], findGutsWinner([2,2,10],[14,13,12]))
        self.assertEqual([2,2,10], findGutsWinner([14,13,12], [2,2,10]))
        self.assertEqual([14,14,10], findGutsWinner([14,14,10], [3,3,14]))
        self.assertEqual([14,3,14], findGutsWinner([3,3,10], [14,3,14]))
    
    def test_high(self):
        self.assertEqual([2,3,5], findGutsWinner([2,3,4], [2,3,5]))

    def test_big_hand(self):
        self.assertEqual([], findGutsWinner([2,3,4], [2,3,5,6]))

    def test_small_hand(self):
        self.assertEqual([], findGutsWinner([2,3], [2,3,5]))


if __name__ == '__main__':
    unittest.main()
