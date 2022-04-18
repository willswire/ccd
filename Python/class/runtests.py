import unittest
from testfile import *
from unittest.mock import patch 
from io import StringIO

class CheckRideTestOne(unittest.TestCase):
    def test_created_correctly(self):
        jokem = Player("Jokem")
        self.assertEqual("Jokem", jokem.name)
        self.assertAlmostEqual((0, 0), jokem.report_pos())
        self.assertAlmostEqual(100.0, jokem.health)

    def test_all_custom(self):
        uther = Player("Uther", 35, 4, 0)
        self.assertEqual("Uther", uther.name)
        self.assertAlmostEqual((4, 0), uther.report_pos())
        self.assertAlmostEqual(35.0, uther.health)

class CheckRideTestTwo(unittest.TestCase):
    def test_move(self):
        jokem = Player("Jokem")
        coord = (5.0,5.0)
        jokem.move(5.0,5.0)
        self.assertAlmostEqual(coord, jokem.report_pos())
        jokem.move(25.0,50.0)
        self.assertAlmostEqual((30.0,55.0), jokem.report_pos())


class CheckRideTestThree(unittest.TestCase):
    def test_health(self):
        jokem = Player("Jokem")
        jokem.move(100,-100)
        self.assertAlmostEqual(29.289321881345245, jokem.health)

        with patch('sys.stdout', new = StringIO()) as mock_out:
            self.assertAlmostEqual(jokem.move(100,-100),0)
            self.assertEqual(mock_out.getvalue(),  'You are out of hit points!\n')

    def test_small_fall(self):
        jokem = Player("Jokem")
        jokem.move(-100,-1)
        self.assertAlmostEqual(100.0, jokem.health)


if __name__ == '__main__':
    unittest.main()
