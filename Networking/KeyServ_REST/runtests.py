import unittest
import hashlib
from client import *


class NetworkUnitTest(unittest.TestCase):
    def is_hex(self, input_string: str) -> bool:
        # Determine if the string represents a hex number
        if len(input_string.strip()) == 0:
            # In case this is an empty string
            return False
        
        for letter in input_string.upper():
            if not (('0' <= letter <= '9') or ('A' <= letter <= 'F')):
                # In case the string is NOT a hex number
                return False
        # If we get this far then the string is a hex number
        return True

    def test_do_key(self):
        key_val = do_key()
        self.assertEqual(128, len(key_val), msg="Mismatch in expected data length")
        self.assertTrue(self.is_hex(key_val.decode()), msg="Expected data to contain hex only")

    def test_do_put(self):
        expected = "3afbea9957cf2eaf8941f91c1f4f045f48d94fe6b4dbbd59b79371505540e15e9d34ae1e66730570c338030b3679dddb" \
                   "2623b1de991caf36ea299754f3b47b03"
        result = do_put(do_key())
        self.assertIsInstance(result, str, msg=f"Expected a string but received {type(result)}")
        self.assertEqual(expected, hashlib.sha512(result.encode()).hexdigest(), 
                         msg="Mismatch in expected server response")


if __name__ == '__main__':
    unittest.main()
