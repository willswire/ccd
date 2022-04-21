import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_BPlus(self):
        avg, final = computeGPA([94, 87, 92, 90, 78, 82])
        
        self.assertEqual(final, "B+")
        self.assertEqual(avg, 3.67)
        
    def test_invalid_score_1(self):
        self.assertEqual("INVALID SCORE", computeGPA([94, 87, 92, 90, 78, 82, 101]))

    def test_invalid_score_2(self):
        self.assertEqual("INVALID SCORE", computeGPA([94, 87, 92, 90, 78, 82, -1]))
        
    def test_hundred_zero(self):
        avg, final = computeGPA([94, 87, 92, 90, 78, 82, 100, 0])
        
        self.assertEqual(final, "B+")
        self.assertEqual(avg, 3.57)

    def test_B(self):
        avg, final = computeGPA([94, 87, 92, 90, 78, 82, 70, 77])
        
        self.assertEqual(final, "B")
        self.assertEqual(avg, 3.28)
                                                                                                                                                                           
    def test_B2(self):
        avg, final = computeGPA([62, 87, 92, 90, 78, 82, 70, 77])
        
        self.assertEqual(final, "B")
        self.assertEqual(avg, 3.0)  

    def test_BMinus(self):
        avg, final = computeGPA([62, 64, 92, 90, 78, 82, 70, 77])
        
        self.assertEqual(final, "B-")
        self.assertEqual(avg, 2.73)          
           
    def test_AMinus(self):
        avg, final = computeGPA([99, 93, 94, 90, 99, 93, 70, 77])
        
        self.assertEqual(final, "A-")
        self.assertEqual(avg, 3.95)  
           
    def test_A(self):
        avg, final = computeGPA([99, 93, 94, 94, 99, 93, 70, 77])
        
        self.assertEqual(final, "A")
        self.assertEqual(avg, 4.0)                                                                                                                                                                                  

    def test_C(self):
        avg, final = computeGPA([62, 77, 73, 90, 78, 70, 70, 72, 74, 0, 77])
        
        self.assertEqual(final, "C")
        self.assertEqual(avg, 2.19)                                                                                                                                                                                  
                                                                                                                                                                                 
    def test_CPlus(self):
        avg, final = computeGPA([62, 77, 73, 90, 78, 70, 70, 72, 74, 82, 84, 77])
        
        self.assertEqual(final, "C+")
        self.assertEqual(avg, 2.37)  

    def test_CMinus(self):
        avg, final = computeGPA([62, 77, 73, 70, 78, 70, 70, 72, 74, 66, 67, 66])
        
        self.assertEqual(final, "C-")
        self.assertEqual(avg, 1.77)          
                                                                                                                                                                                                                                                                                                                                                                 
    def test_D(self):
        avg, final = computeGPA([62, 60, 55, 70, 59, 70, 70, 72, 74, 66, 67, 66])
        
        self.assertEqual(final, "D")
        self.assertEqual(avg, 1.21) 
        
    def test_F(self):
        avg, final = computeGPA([62, 27, 45, 70, 78, 55, 70, 53, 0, 0, 67, 66])
        
        self.assertEqual(final, "F")
        self.assertEqual(avg, 0.8)                                                                                                                                                                                                                                                                                                                                                                  
    
          
if __name__ == '__main__':
    unittest.main()
