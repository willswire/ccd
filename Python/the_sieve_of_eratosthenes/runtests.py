import unittest
from testfile import *
from data import *


class CheckRideTestOne(unittest.TestCase):
    def test_sieve_of_Eratosthenes(self):
        prime_list = sieve_of_Eratosthenes()
        self.assertEqual(set(prime_list), set(prime_numbers_less_than_1000))


if __name__ == '__main__':
    unittest.main()
