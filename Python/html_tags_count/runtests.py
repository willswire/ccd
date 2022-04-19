import unittest
from testfile import *
from data import *


class CheckRideTestOne(unittest.TestCase):
    def test_HTML_count_tags(self):
        self.assertEqual([1, 1, 1], HTML_count_tags(HTML_files[0]))
        self.assertEqual([1, 2], HTML_count_tags(HTML_files[1]))
        self.assertEqual([1, 3, 4], HTML_count_tags(HTML_files[2]))


if __name__ == '__main__':
    unittest.main()
