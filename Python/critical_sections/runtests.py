import unittest, time
from testfile import *

##########################################################
# Unable to unit test much more w/o giving away the answer
##########################################################


class AddThreadTest(unittest.TestCase):
    def test_add_thread_created(self):
        threadName = "add_thread_test1"
        lock = threading.RLock()
        add_thread = AddThread(threadName, lock)
        self.assertEqual(threadName, add_thread.name)


class MultiplyThreadTest(unittest.TestCase):
    def test_multiply_thread_created(self):
        threadName = "multiply_thread_test1"
        lock = threading.RLock()
        multiply_thread = MultiplyThread(threadName, lock)
        self.assertEqual(threadName, multiply_thread.name)


if __name__ == '__main__':
    unittest.main()
