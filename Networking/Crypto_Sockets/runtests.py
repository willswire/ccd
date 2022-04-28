from client import create_fernet_and_find_sign_key
import unittest
import hashlib
import time
from client import *

valid_msg = [
    "cfb166742fe8d6c8f0358caef77e3aa5e7f70ae4e6bf3e23e9c4050483997c9b",
    "2a05fc13b86b39d4fe33da663929685670eaee860d956681e07ee9cb446f5b75",
    "ca0b6efe87b26cd899850716ad8dea9ab6ebc811bcb5b756efb4579d7377dcdb",
    "948b4ccb0d9af19ad8184a757ca4b5fea81f54d5b13fcb9196867cb165012d4e",
    "e516ad9e09acd9bbc57b61688fb8f9e737517fe30111e711c038343ab407dfa7",
    "673c97f2693516da72a569ba79e56fab2ad6bdd0235e576812d50f9ba8b1db1a",
    "afb8888511ac6a97bc10101e55fe08690791d1c4bffa78fcbeb1bf52a2de7480",
    "4f538605b919075d0b30d39cc83ddd626be442ea6171f93bec253892233502b1",
    "ecab980de9134238f3e93d727d2018076d651bd061b083a5d8774f3b16bea80c",
    "f73783028bd15517bbd7f54a4a7d752395f3f3feed86fc5e5447cbbd42c982e0"
]

valid_key = b"cmbnavlzr9_sm6V8j4Bnx0JTPqIdpsdfHC8sh291wGw="
expected_skey = "ed846366519ceb232e43fd5a4bd4aba5b3fc71ea99c14be6265afe0962b2dedf"
expected_ekey = "6aa0d448c369f76d3f89209775f389c134d1e66cafc0196e55fe4837a18e2431"


class NetworkUnitTest(unittest.TestCase):
    def setUp(self):
        self.wait_time = 0.5

    def test_create_fernet_and_find_sign_key_intrusion_event(self):
        error_msg = "Potential Intrusion Event Detected."
        key = b"123DE45^-h"
        with self.assertRaises(ValueError) as cm:
            create_fernet_and_find_sign_key(key)
        self.assertEqual(error_msg, cm.exception.args[0], 
                         msg=f"Mismatch in error msg: expected '{error_msg}' but received '{cm.exception.args[0]}'")
    
    def test_create_fernet_and_find_sign_key_valid_key(self):
        f_key, sign = create_fernet_and_find_sign_key(valid_key)
        self.assertIsInstance(f_key, Fernet, 
                              msg=f"Mismatch in object: expected a Fernet object but received '{type(f_key)}'")
        self.assertEqual(expected_skey, hashlib.sha256(f_key._signing_key).hexdigest(), 
                         msg="Mismatch in Fernet object's signing key")
        self.assertEqual(expected_ekey, hashlib.sha256(f_key._encryption_key).hexdigest(), 
                         msg="Mismatch in Fernet object's encrption key")
        self.assertEqual(expected_skey, hashlib.sha256(sign).hexdigest(), msg="Mismatch in expected signing key")

    def test_crypto(self):
        msg_valkey = "Mismatch in response: expected message indicating a valid key"
        msg_intevt = "Mismatch in response: expected message indicating an intrusion event"
        for attempt in range(20):
            is_valkey_msg = False
            # Run multiple tests to ensure we test the client sent message as well as the server received messages
            response = dowork()
            if type(response) == type(b""):
                is_valkey_msg = True
                response = hashlib.sha256(response).hexdigest()
            else:
                response = hashlib.sha256(response.encode()).hexdigest()
            if is_valkey_msg:
                self.assertTrue(response in valid_msg, msg_valkey)
            else:
                self.assertTrue(response in valid_msg, msg_intevt)
            time.sleep(self.wait_time)  # In order to prevent overloading the server


if __name__ == '__main__':
    unittest.main()
