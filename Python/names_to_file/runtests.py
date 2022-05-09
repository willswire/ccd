import unittest
from testfile import *


goodNames = ["Aaron, Hank",
            "Grey, Earl",
            "James, George",
            "Jones, Bill",
            "Reeves, Keanu",
            "Smith, John"]

names = [["Bill","jones"], 
        ["John","Smith"], 
        ["george","james"], 
        ["Hank","Aaron"], 
        ["Earl","Grey"],
        ["Keanu","Reeves"]]


class CheckRideTestOne(unittest.TestCase):
    def test_files(self):
        self.assertEqual("SUCCESS", create_file(names))
        
        i = 0
        try:
            f = open("names.txt","r")
            for line in f:
                fullName = line.rstrip()
                
                self.assertEqual(fullName, goodNames[i])
                i += 1
            f.close()
        except IOError:
            #unable to open file
            self.assertEqual("GOOD_FILE","BAD_FILE")
            
        #check if file has same number of names
        self.assertEqual(i, len(goodNames))

    def test_empty(self):
        names = []
        self.assertEqual("EMPTY_LIST", create_file(names))
        
    def test_invalid_name(self):
        names = [["Bill","jones"],["John"],["Rick","Jones"],["Hank","Aaron"]]
        self.assertEqual("INVALID_NAME", create_file(names))
        
        names = [[],["John","Smith"],["Rick",""],["Hank","Aaron"]]
        self.assertEqual("INVALID_NAME", create_file(names))
        
        names = [["John","Smith","Jr"],["Rick",""],["Hank","Aaron"]]
        self.assertEqual("INVALID_NAME", create_file(names))


if __name__ == '__main__':
    unittest.main()
