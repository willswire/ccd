import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_recursive(self):
        ul = [8, 2, 3, 9, 1, 44, 22, 11, 90, 0]
        ol = [0, 1, 2, 3, 8, 9, 11, 22, 44, 90]

        oList = createOrderedList(ul)

        self.assertEqual(len(ol), len(oList))  # list is right len
        for i in range(len(oList)):
            self.assertEqual(ol[i], oList[i])

        idx = binarySearch(oList, 0, len(oList) - 1, 44)
        self.assertEqual(idx, 8)

        idx = binarySearch(oList, 0, len(oList) - 1, 2)
        self.assertEqual(idx, 2)

        idx = binarySearch(oList, 0, len(oList) - 1, 11)
        self.assertEqual(idx, 6)

        idx = binarySearch(oList, 0, len(oList) - 1, 90)
        self.assertEqual(idx, 9)

        idx = binarySearch(oList, 0, len(oList) - 1, 0)
        self.assertEqual(idx, 0)

        idx = binarySearch(oList, 0, len(oList) - 1, 10)
        self.assertEqual(idx, -1)

    def test_recursive2(self):
        oList = createOrderedList([5])  #one element list
        self.assertEqual(1, len(oList))
        idx = binarySearch(oList, 0, len(oList) - 1, 5)
        self.assertEqual(idx, 0)

    def test_recursive3(self):
        oList = createOrderedList([]) #empty list

        self.assertEqual(0, len(oList))

        idx = binarySearch(oList, 0, len(oList) - 1, 1)
        self.assertEqual(idx, -2)


if __name__ == '__main__':
    unittest.main()
