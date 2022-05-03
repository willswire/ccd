import unittest
import hashlib
from client import *


class NetworkUnitTest(unittest.TestCase):
    def setUp(self):
        self.expectedMode = '61c88aa59a29957f71becdf52072c96fb07e1357de1cd7b2e85fd17c0adfbf1d'
        self.expectedKey = '9d82d3baedcc2a20155229a15c3140213a63cf001774a00187892a5784a5b892'
    
    
    def test_sending_data(self):
        recv = query_mode()
        mode = recv[1]
        self.assertEqual('0x800', hex(recv[0]))
        self.assertEqual(self.expectedMode, hashlib.sha3_256((mode).to_bytes(4, byteorder='big')).hexdigest())
        response = get_key(recv)
        self.assertEqual(self.expectedKey, hashlib.sha3_256(response.encode()).hexdigest())

if __name__ == '__main__':
   unittest.main()
