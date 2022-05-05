import unittest
from testfile import *
import sys


class CheckRideTestOne(unittest.TestCase):
    def test_remove_extra_spaces_corner_cases(self):
        self.assertEqual("The input sentence does not contain extra spacing",
            remove_extra_spaces("The input sentence does not contain extra spacing"))
        self.assertEqual("The input sentence does not contain extra spacing",
            remove_extra_spaces("Welcome to Python Programming"))

    def test_remove_extra_spaces(self):
        self.assertEqual("Hello World", remove_extra_spaces("Hello World "))
        self.assertEqual("Hello World", remove_extra_spaces(" Hello World"))
        self.assertEqual("Hello World", remove_extra_spaces(" Hello World "))
        self.assertEqual("Welcome to Python Programming", remove_extra_spaces(" Welcome to   Python   Programming "))


if __name__ == '__main__':
    unittest.main()
