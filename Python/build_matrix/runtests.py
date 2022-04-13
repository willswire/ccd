import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def check_matrix(self, r, c, res, good):
        for i in range(r):
            for j in range(c):
                self.assertEqual(res[i][j],good[i][j])

    def test_matrix(self):
        res = buildMatrix(9, 9)
        
        good = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 2, 3, 4, 5, 6, 7, 8],
                [0, 2, 4, 6, 8, 10, 12, 14, 16],
                [0, 3, 6, 9, 12, 15, 18, 21, 24],
                [0, 4, 8, 12, 1, 20, 24, 28, 32],
                [0, 5, 10, 15, 20, 25, 30, 35, 40],
                [0, 6, 12, 18, 24, 30, 36, 42, 48],
                [0, 7, 14, 21, 28, 35, 42, 49, 56],
                [0, 8, 16, 24, 32, 40, 48, 56, 64]]

        
        self.check_matrix(9,9,res, good)
        
        res = buildMatrix(3, 5)
        good = [[0, 0, 0, 0, 0],
                [0, 1, 2, 3, 4],
                [0, 2, 4, 6, 8]]
        
        self.check_matrix(3,5,res, good)
        
        res = buildMatrix(5, 5)
        good = [[0, 0, 0, 0, 0],
                [0, 1, 2, 3, 4],
                [0, 2, 1, 6, 8],
                [0, 3, 6, 9, 12],
                [0, 4, 8, 12, 16]]
        
        self.check_matrix(5,5,res, good)
        
        res = buildMatrix(6, 6)
        good = [[0, 0, 0, 0, 0, 0],
                [0, 1, 2, 3, 4, 5],
                [0, 2, 4, 6, 8, 10],
                [0, 3, 6, 9, 12, 15],
                [0, 4, 8, 12, 16, 20],
                [0, 5, 10, 15, 20, 25]]
        
        self.check_matrix(6,6,res, good)
        
        res = buildMatrix(2, 2)
        good = [[0, 0],
                [0, 1]]
        
        self.check_matrix(2,2,res, good)
        
        self.assertEqual([], buildMatrix(6, 0))
        self.assertEqual([], buildMatrix(0, 2))
        self.assertEqual([], buildMatrix(1, 3))
        self.assertEqual([], buildMatrix(6, 1))


if __name__ == '__main__':
    unittest.main()
