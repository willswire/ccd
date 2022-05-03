import unittest
import hashlib
from binascii import unhexlify
from client import *


class NetworkUnitTest(unittest.TestCase):
    hashval = "cb818d754fdabb262721d62ce968a940759fd5c03877e8672846f23d92c13b76"
    serv_msg = "dcc17565ec3eaef5600750ef41edd0e2e9f25e07c1b3883bc01f8e2e7ee9fe57"
    def test_keys(self):
        response, key = match_keys()
        self.assertEqual(self.serv_msg, hashlib.sha256(response).hexdigest(), msg="Unsucessful server response")
        self.assertIsNotNone(key)
        self.assertEqual(self.hashval, hashlib.sha256(key.encode()).hexdigest(), msg="Incorrect key")


if __name__ == '__main__':
    unittest.main()
