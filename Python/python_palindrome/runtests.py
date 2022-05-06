import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual("palindrome", palindrome(00000))
        self.assertEqual("palindrome", palindrome(12321))
        self.assertEqual("palindrome", palindrome(55555))
        self.assertEqual("palindrome", palindrome(45554))
        self.assertEqual("palindrome", palindrome(11611))

    def test_not_palindrome(self):
        self.assertEqual("NOT a palindrome", palindrome(12345))
        self.assertEqual("NOT a palindrome", palindrome(10012))


if __name__ == '__main__':
    unittest.main()
