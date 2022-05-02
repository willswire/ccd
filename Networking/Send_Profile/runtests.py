import unittest
import hashlib
from client import *


class NetworkUnitTest(unittest.TestCase):
    uc_key = "usr_cred"
    uc_value = "f52fbd32b2b3b86ff88ef6c490628285f482af15ddcb29541f94bcf526a3f6c7"
    un_key = "u_name"
    un_value = "0f5c1c2f5581c49fa0b8bb1d614482b2368b1afe519397a14f94797bd41370eb"
    tp_key = "total_posts"
    tp_value = "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
    invfmt = "Invalid format"
    nofile = "File does not exist"
    wlcm_msg = "34e886059aa1ed4b01689bf63b6244f402bd576b0905c650f86695a1904a2c99"
    invcrd = "Invalid credentials"
    invdatafmt = "a8d520db0c8a6107592581cec75f2e75aa0dcb88ce437b6b49701f3c32a5499b"

    def test_read_user_info(self):
        response = read_user_info("user_dat.json")

        self.assertIsInstance(response, dict, msg=f"Expected 'dict' object but received {type(response)} instead")

        self.assertTrue(NetworkUnitTest.uc_key in response, msg=f"Expected key '{NetworkUnitTest.uc_key}' not found")
        self.assertEqual(type(''), type(response[NetworkUnitTest.uc_key]),
                         msg=f"Expected 'str' object but received {type(response[NetworkUnitTest.uc_key])} instead")
        self.assertEqual(NetworkUnitTest.uc_value, 
                         hashlib.sha256(response[NetworkUnitTest.uc_key].encode()).hexdigest(),
                         msg=f"Mismatch in expected {NetworkUnitTest.uc_key} value")

        self.assertTrue(NetworkUnitTest.un_key in response, msg=f"Expected key '{NetworkUnitTest.un_key}' not found")
        self.assertEqual(type(''), type(response[NetworkUnitTest.un_key]),
                         msg=f"Expected 'str' object but received {type(response[NetworkUnitTest.un_key])} instead")
        self.assertEqual(NetworkUnitTest.un_value, 
                         hashlib.sha256(response[NetworkUnitTest.un_key].encode()).hexdigest(),
                         msg=f"Mismatch in expected {NetworkUnitTest.un_key} value")

        self.assertTrue(NetworkUnitTest.tp_key in response, msg=f"Expected key '{NetworkUnitTest.tp_key}' not found")
        self.assertEqual(type(1), type(response[NetworkUnitTest.tp_key]),
                         msg=f"Expected 'int' object but received {type(response[NetworkUnitTest.tp_key])} instead")
        self.assertEqual(NetworkUnitTest.tp_value, 
                         hashlib.sha256(str(response[NetworkUnitTest.tp_key]).encode()).hexdigest(),
                         msg=f"Mismatch in expected {NetworkUnitTest.tp_key} value")

    def test_read_invalid_json(self):
        response = read_user_info("user_text.txt")
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.invfmt, response, msg="Mismatch in expected ERROR message")

    def test_read_no_file(self):
        response = read_user_info("missing_file.dat")
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.nofile, response, msg="Mismatch in expected ERROR message")

    def test_sending_valid_data(self):
        u_dat = {
            NetworkUnitTest.uc_key: "hunter2",
            NetworkUnitTest.un_key: "crashoverride",
            NetworkUnitTest.tp_key: 123
        }
        response = send_user_data(u_dat)
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.wlcm_msg, hashlib.sha256(response.encode()).hexdigest(), 
                         msg="Mismatch in returned server WELCOME message")
    
    def test_sending_invalid_cred(self):
        u_dat = {
            NetworkUnitTest.uc_key: "12345",
            NetworkUnitTest.un_key: "crashoverride",
            NetworkUnitTest.tp_key: 123
        }
        response = send_user_data(u_dat)
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.invcrd, response, msg="Mismatch in returned server ERROR message")

    def test_sending_missing_user(self):
        u_dat = {
            NetworkUnitTest.uc_key: "hunter2",
            NetworkUnitTest.tp_key: 123
        }
        response = send_user_data(u_dat)
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.invdatafmt, hashlib.sha256(response.encode()).hexdigest(), 
                         msg="Mismatch in returned server ERROR message")

    def test_sending_missing_total(self):
        u_dat = {
            NetworkUnitTest.uc_key: "hunter2",
            NetworkUnitTest.un_key: "crashoverride"
        }
        response = send_user_data(u_dat)
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.invdatafmt, hashlib.sha256(response.encode()).hexdigest(), 
                         msg="Mismatch in returned server ERROR message")

    def test_logon_valid(self):
        response = logon("user_dat.json")
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.wlcm_msg, hashlib.sha256(response.encode()).hexdigest(), 
                         msg="Mismatch in returned server WELCOME message")

    def test_logon_invalid_json(self):
        response = logon("user_text.txt")
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.invfmt, response, msg="Mismatch in expected ERROR message")

    def test_logon_no_file(self):
        response = logon("file_doesnt_exist.txt")
        self.assertIsInstance(response, str, msg=f"Expected 'str' object but received {type(response)} instead")
        self.assertEqual(NetworkUnitTest.nofile, response, msg="Mismatch in expected ERROR message")


if __name__ == '__main__':
    unittest.main()
