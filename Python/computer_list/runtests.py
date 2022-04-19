import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_computers(self):
        good = [Computer("Lenovo", "Thinkpad X1", 795.95, 16, 512),
            Computer("HP", "Ideapad", 595, 8, 128),
            Computer("HP", "Pavillion", 619.99, 8, 256),
            Computer("Dell", "Inspiron 5000", 689, 8, 128),
            Computer("Lenovo", "X390", 749.50, 8, 512),
            Computer("HP", "Envy", 899.00, 8, 256),
            Computer("HP", "Omen", 799.99, 8, 256)]
        
        res = create_computer_objects("computers.txt")

        for i in range(len(good)):
            self.assertEqual(good[i], res[i])
    
    def test_edge_cases(self):
        edge = [Computer("Lenovo", "Thinkpad X1", 795.95, 16, 512),
            Computer("HP", "Pavillion", 619.99, 8, 256),
            Computer("Dell", "Inspiron 5000", 689, 8, 128),
            Computer("Lenovo", "X390", 749.50, 8, 512),
            Computer("HP", "Omen", 799.99, 8, 256)]

        res = create_computer_objects("computers4.txt")
        for i in range(len(edge)):
            self.assertEqual(edge[i], res[i])
    
    def test_invalid(self):
        with self.assertRaises(ValueError) as e:
            create_computer_objects("computers2.txt")
        self.assertEqual("INVALID DATA", str(e.exception))

        with self.assertRaises(ValueError) as e:
            create_computer_objects("computers3.txt")
        self.assertEqual("INVALID DATA", str(e.exception))
    
    def test_no_file(self):
        with self.assertRaises(FileNotFoundError) as e:
            create_computer_objects("bad.txt")
        self.assertEqual("FILE CORRUPTED", str(e.exception))


if __name__ == '__main__':
    unittest.main()
