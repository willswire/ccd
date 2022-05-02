import unittest
import hashlib
from client import *


class NetworkUnitTest(unittest.TestCase):
    expected_str_hash = 'c93fc1ebee779045574aaac6aad7e6f0ac9e2b545efdd4dd6ed03c8bcee163e1'
    expected_val_hash = '8b940be7fb78aaa6b6567dd7a3987996947460df1c668e698eb92ca77e425349'
    
    def test_sending_data(self):
        response_str, response_val = send_the_data()
        self.assertEqual(hashlib.sha256(response_str.encode()).hexdigest(), self.expected_str_hash)
        self.assertEqual(hashlib.sha256(str(response_val).encode()).hexdigest(), self.expected_val_hash)

if __name__ == '__main__':
    unittest.main()
