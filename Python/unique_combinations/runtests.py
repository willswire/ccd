import unittest
from testfile import *
from collections import Counter
from math import factorial

import functools
import random
import string
import unittest

MAX_TEST = 6


class TestCombinator(unittest.TestCase):
    def setUp(self):
        self.test_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(MAX_TEST))

    def test_using_generated(self):
        self.assertEqual(count_unique_permutations(self.test_string), self.math_solution(self.test_string))

    def test_using_static(self):
        self.assertEqual(count_unique_permutations('aaaabccca'), 504)
        self.assertEqual(count_unique_permutations('aaab'), 4)
        self.assertEqual(count_unique_permutations('aaaa'), 1)

    @staticmethod
    def math_solution(input_str):
        numerator = factorial(len(input_str))
        cnt = Counter(input_str)
        frequencies = filter(lambda x: x > 1, cnt.values())
        facts = map(factorial, frequencies)

        try:
            denominator = functools.reduce(lambda x, y: x * y, facts)
        except TypeError:
            denominator = 1

        return numerator / denominator


if __name__ == '__main__':
    unittest.main()
