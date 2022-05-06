import unittest
from testfile import *


class CheckRideTests(unittest.TestCase):
    def setUp(self) -> None:
        self.myQueue = queue()
        self.msg_queue_class = "Not an instance of class 'queue'"
        self.msg_queue_constructor = "Queue not empty"
        self.msg_dequeue = "Error while using dequeue()"
        self.msg_enqueue = "Error while using enqueue()"
        self.msg_size = "Error while using size()"
        self.msg_mtqueue = "Error while using emptyQueue()"
        self.msg_peek = "Error while using peek()"
        self.msg_ismt = "Error while using isEmpty()"

    def test_queue_class(self):
        self.assertIsInstance(self.myQueue, queue, msg=self.msg_queue_class)

    def test_empty_queue(self):
        expected = []
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_queue_constructor)

    def test_add_mt_list(self):
        expected = []
        self.myQueue.enqueue(expected)  # Try and add zero items
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_enqueue)

    def test_add_4_items(self):
        expected = [5, 2, 7, 9]
        self.myQueue.enqueue(expected)  # Try and add four items
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_enqueue)

    def test_add_7_items(self):
        expected = [7, 9, 0, 22, 32, 12, 99]
        self.myQueue.enqueue(expected)  # Try and add seven items
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_enqueue)

    def test_dequeue_mt_queue(self):
        expected = []
        self.myQueue.dequeue(2)  # Try and remove items from an empty queue
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_dequeue)

    def test_dequeue_0_queue_content(self):
        items = [7, 9, 0, 22, 32, 12, 99]
        expected = [7, 9, 0, 22, 32, 12, 99]
        self.myQueue.qList = items  # Setup the test queue with values
        self.myQueue.dequeue(0)  # Try and remove zero items
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_dequeue)

    def test_dequeue_gt_0_lt_queue_content(self):
        items = [7, 9, 0, 22, 32, 12, 99]
        expected = [22, 32, 12, 99]
        self.myQueue.qList = items  # Setup the test queue with values
        self.myQueue.dequeue(3)  # Try and remove three items
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_dequeue)

    def test_dequeue_eq_queue_content(self):
        items = [0, 22, 32, 7, 9]
        expected = []
        self.myQueue.qList = items  # Setup the test queue with values
        self.myQueue.dequeue(5)  # Try and remove five items
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_dequeue)

    def test_dequeue_gt_queue_content(self):
        items = [5, 2, 7, 9]
        expected = [5, 2, 7, 9]
        self.myQueue.qList = items  # Setup the test queue with values
        self.myQueue.dequeue(5)  # Try and remove five items
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_dequeue)

    def test_size_0_queue_content(self):
        expected = []
        self.assertEqual(len(expected), self.myQueue.size(), msg=self.msg_size)

    def test_size_1_queue_content(self):
        expected = [1234623]
        self.myQueue.qList = expected  # Setup the test queue with values
        self.assertEqual(len(expected), self.myQueue.size(), msg=self.msg_size)

    def test_size_4_queue_content(self):
        expected = [5, 2, 7, 9]
        self.myQueue.qList = expected  # Setup the test queue with values
        self.assertEqual(len(expected), self.myQueue.size(), msg=self.msg_size)

    def test_size_11_queue_content(self):
        expected = [5, 2, 7, 9, 7, 9, 0, 22, 32, 12, 99]
        self.myQueue.qList = expected  # Setup the test queue with values
        self.assertEqual(len(expected), self.myQueue.size(), msg=self.msg_size)

    def test_mtqueue_0_items(self):
        expected = []
        self.myQueue.emptyQueue()  # Try to delete everything from an empty queue
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_mtqueue)

    def test_mtqueue_4_items(self):
        items = [5, 2, 7, 9]
        expected = []
        self.myQueue.qList = items  # Setup the test queue with values
        self.myQueue.emptyQueue()  # Try to delete everything from a 4 item queue
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_mtqueue)

    def test_mtqueue_11_items(self):
        items = [5, 2, 7, 9, 7, 9, 0, 22, 32, 12, 99]
        expected = []
        self.myQueue.qList = items  # Setup the test queue with values
        self.myQueue.emptyQueue()  # Try to delete everything from an 11 item queue
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_mtqueue)

    def test_peek_0_items(self):
        expected = []
        self.assertIsNone(self.myQueue.peek(), msg=self.msg_peek)
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_peek)

    def test_peek_1_item(self):
        expected = [32]
        expected_peek = 32
        self.myQueue.qList = expected  # Setup the test queue with values
        self.assertEqual(expected_peek, self.myQueue.peek(), msg=self.msg_peek)
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_peek)

    def test_peek_4_item(self):
        expected = [9, 0, 22, 32]
        expected_peek = 9
        self.myQueue.qList = expected  # Setup the test queue with values
        self.assertEqual(expected_peek, self.myQueue.peek(), msg=self.msg_peek)
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_peek)

    def test_peek_11_item(self):
        expected = [541, 2, 7, 9, 7, 9, 0, 22, 32, 12, 99]
        expected_peek = 541
        self.myQueue.qList = expected  # Setup the test queue with values
        self.assertEqual(expected_peek, self.myQueue.peek(), msg=self.msg_peek)
        self.assertListEqual(expected, self.myQueue.qList, msg=self.msg_peek)

    def test_is_mt_0_items(self):
        self.assertTrue(self.myQueue.isEmpty(), msg=self.msg_ismt)

    def test_is_mt_1_item(self):
        items = [79]
        self.myQueue.qList = items  # Setup the test queue with values
        self.assertFalse(self.myQueue.isEmpty(), msg=self.msg_ismt)

    def test_is_mt_4_items(self):
        items = [5, 2, 7, 9]
        self.myQueue.qList = items  # Setup the test queue with values
        self.assertFalse(self.myQueue.isEmpty(), msg=self.msg_ismt)

    def test_is_mt_11_items(self):
        items = [5, 2, 7, 9, 7, 9, 0, 22, 32, 12, 99]
        self.myQueue.qList = items  # Setup the test queue with values
        self.assertFalse(self.myQueue.isEmpty(), msg=self.msg_ismt)


if __name__ == '__main__':
    unittest.main()
