import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(286, computeVolume(4, [2,3,3]))
        self.assertEqual(286, computeVolume([2,3,3], 4))
        self.assertEqual(5, computeVolume(1, [1,1,1]))
        self.assertEqual(529599, computeVolume(50, [10,20,30]))

    def test_invalid(self):
        self.assertEqual("INVALID", computeVolume([2,-3,3], 4))
        self.assertEqual("INVALID", computeVolume([2,3,3], -4))
        self.assertEqual("INVALID", computeVolume(1, [1,0,1]))
        self.assertEqual("INVALID", computeVolume([2,4,5], 0))
        self.assertEqual("INVALID", computeVolume(0, [2,3,3]))
        self.assertEqual("INVALID", computeVolume([], [2,3,3]))
        self.assertEqual("INVALID", computeVolume(2, [2,3]))
        self.assertEqual("INVALID", computeVolume([2,3], 2))
        self.assertEqual("INVALID", computeVolume(2, 2))
        self.assertEqual("INVALID", computeVolume([], [2,3,3,7]))
        self.assertEqual("INVALID", computeVolume([2,3,3], [2,3,3]))


if __name__ == '__main__':
    unittest.main()
