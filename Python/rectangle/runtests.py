import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def setUp(self):
        self.test_rect = Rectangle((4.0, 8.0), (8.0, 2.0))
        self.test_square = Rectangle((3.0, 5.0), (5.0, 3.0))

    def test_length(self):
        self.assertEqual(6.0, self.test_rect.length())
        self.assertEqual(2.0, self.test_square.length())

    def test_width(self):
        self.assertEqual(4.0, self.test_rect.width())
        self.assertEqual(2.0, self.test_square.width())

    def test_perimeter(self):
        self.assertEqual(20.0, self.test_rect.perimeter())
        self.assertEqual(8.0, self.test_square.perimeter())

    def test_area(self):
        self.assertEqual(24.0, self.test_rect.area())
        self.assertEqual(4.0, self.test_square.area())

    def test_is_square(self):
        self.assertEqual(0, self.test_rect.isSquare())
        self.assertEqual(1, self.test_square.isSquare())

    def test_err(self):
        with self.assertRaises(ValueError):
            Rectangle((0.0, 0.0), (0.0, -8.0))


if __name__ == '__main__':
    unittest.main()
