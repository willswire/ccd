import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_shapes(self):
        shapeList = [[40,50,90], [60,70,80], [45,55,80], [10,20,30],
          [90,100,-10], [100,100,-200], [120,60,0], [60,60,60], [90,90,0],
          [40,60,80], [1,1,178], [1,90,89]]
        resDict = classify_shapes(shapeList)
        self.assertEqual(2, resDict["triRight"])
        self.assertEqual(1, resDict["triEquilateral"])
        self.assertEqual(3, resDict["triOther"])
        self.assertEqual(6, resDict["triInvalid"])

    def test_empty_shapes(self):
        shapeList= []
        self.assertEqual("EMPTY_LIST", classify_shapes(shapeList))
        self.assertEqual("EMPTY_LIST", classify_shapes(None))

    def test_invalid_shapes(self):
        # list with 4 elements
        shapeList = [[40,50,90], [60,70,80], [45,55,80], [10,20,30], [10,20,30,300],
          [90,90,90,91], [90,90,90,90], [90,100,-10], [100,100,-200],
          [120,60,0], [120,120], [200,100,40,20], [360,0,0,0],
          [60,60,60]]
        self.assertEqual("INVALID_LIST", classify_shapes(shapeList))

        # list with only two elements
        shapeList = [[40,50,90], [60,70,80], [45,55,80], [10,20,30],
          [90,100,-10], [100,100,-200], [120,60,0], [120,120],
          [60,60,60]]
        self.assertEqual("INVALID_LIST", classify_shapes(shapeList))


if __name__ == '__main__':
    unittest.main()
