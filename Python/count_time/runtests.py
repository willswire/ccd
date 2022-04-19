import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_good_files(self):
        good = [['bbergner', 46], ['rboone', 44], ['ecruz', 43], ['dfarr', 42], ['jwarren', 38]]
        small = [['ecruz', 44], ['rboone', 34], ['dgilles', 26], ['jwarren', 14]]
        culprits = find_culprits("mainList.txt")
        self.assertListEqual(good, culprits)
        self.assertListEqual(small, find_culprits("smallList.txt"))
        
    def test_bad_file(self):
        self.assertIsNone(find_culprits("bad.txt"))

    def test_empty(self):
        self.assertListEqual([], find_culprits("empty.txt"))

    def test_tie(self):
        big_tie = [["bbently", 52],["jdoe", 50],['jsmith', 46], ["cptplaceholder", 46],["tlopez", 38]]
        big_tie2 = [["bbently", 52],["jdoe", 50], ["cptplaceholder", 46],['jsmith', 46],["tlopez", 38]]
        culprits = find_culprits("biggerlist2.txt")
        try:
            self.assertListEqual(big_tie, culprits)
        except AssertionError:
            self.assertListEqual(big_tie2, culprits)

        big_tie = [["bbently", 52],["jdoe", 50],['jsmith', 46], ["cptplaceholder", 42],["tlopez", 38]]
        big_tie2 = [["bbently", 52],["jdoe", 50],['jsmith', 46], ["cptplaceholder", 42],["fgoodman", 38]]
        culprits = find_culprits("biggerlist.txt")
        try:
            self.assertListEqual(big_tie, culprits)
        except AssertionError:
            self.assertListEqual(big_tie2, culprits)

          
if __name__ == '__main__':
    unittest.main()
