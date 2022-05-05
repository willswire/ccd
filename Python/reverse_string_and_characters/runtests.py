#!/usr/bin/env python
import unittest, subprocess, os, re, base64
from testfile import *
from helper_stuff import *


class CheckRideTestOne(unittest.TestCase):
    def test_string_reversal(self):
        exp_input = [
        "abcdefg",
        "hijklmn",
        "opqrstu",
        "vwxyz12",
        ]

        expected_output = "gfedcba nmlkjih utsrqpo 21zyxwv"
        self.assertEqual(expected_output, reverse_strings(exp_input))

    def test_single_reverse(self):
        exp_input = [
            "qwertyu"
        ]

        expected_output = "uytrewq"
        self.assertEqual(expected_output, reverse_strings(exp_input))


if __name__ == '__main__':
    unittest.main()
