import unittest
import hashlib
import os
from content_manager import *

file_1_name = "riddle.txt"
file_1 = "02cf88b8c0c6f4aa8f46656b8123fa19825a1d7162a838d0279ee90cf797eb8a"
file_2_name = "setup.dat"
file_2 = "ba9c822ad636fa32b71d094573a9fd119b6147bbda26997e66e5bf05f65c59a3"



class NetworkUnitTest(unittest.TestCase):
    def test_server(self):
        serve_clients()
        try:
            with open(file_1_name) as f1:
                f1_cont = f1.read()
            self.assertEqual(hashlib.sha256(f1_cont.encode()).hexdigest(), file_1)
            os.remove(file_1_name)
        except FileNotFoundError:
            self.fail("riddle.txt was not found")

        try:
            with open(file_2_name) as f2:
                f2_cont = f2.read()
            self.assertEqual(hashlib.sha256(f2_cont.encode()).hexdigest(), file_2)
            os.remove(file_2_name)
        except FileNotFoundError:
            self.fail("setup.dat was not found")


if __name__ == '__main__':
    unittest.main()
