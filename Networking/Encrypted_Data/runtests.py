import unittest, hashlib
from client import get_message_using_encrypted_request_protocol


class NetworkUnitTest(unittest.TestCase):

    def test_get_message_using_encrypted_request_protocol_correct_type(self):
        print("\nTest 1:  correct return type")
        ret = get_message_using_encrypted_request_protocol()
        self.assertTrue(isinstance(ret, str))

    def test_get_message_using_encrypted_request_protocol_correct_value(self):
        print("\nTest 2:  correct result value")
        ret = get_message_using_encrypted_request_protocol()
        correct_answer_hash = '3fa111debea33dbd62815f6706ab813b'
        your_answer_hash = hashlib.md5(ret.encode("UTF-8")).hexdigest()
        self.assertTrue(your_answer_hash == correct_answer_hash)


if __name__ == '__main__':
    unittest.main()
