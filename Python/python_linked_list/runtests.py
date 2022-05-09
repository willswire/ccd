import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def compare_lists(self, test_linked_list, expected_name_list):
        '''
        Purpose: This compares the test_linked_list nodes to ensure a node exists for each name in expected_name_list.
        :param test_linked_list: The head to a Python singly linked list.
        :param expected_name_list: A list containing the names that should appear in the Python linked list.
        :return: a number representing the number of nodes in the Python linked list.
        '''
        curr:Node = test_linked_list.head
        i:int = 0
        while curr:
            self.assertEqual(curr.name, expected_name_list[i])
            i += 1
            curr = curr.next
        self.assertEqual(len(expected_name_list), i)
        return i

    def test_Node(self):
        testNode = Node("test")
        self.assertTrue(hasattr(testNode, "name"), "Expected name attribute not found")
        self.assertTrue(hasattr(testNode, "next"), "Expected next attribute not found")
        self.assertIsInstance(testNode.name, str, "Expected name to be a string object")
        self.assertIsNone(testNode.next)

    def test_empty_constructor(self):
        empty_list:SingleList = SingleList()
        self.assertIsNone(empty_list.head)
        self.assertIsNone(empty_list.tail)

    # test that the constructor was able to build a linked list using the insert function
    def test_constructor(self):
        name_list:list = ['Joe','Jack','Aaron','Bill','Sally','George']
        test_list:SingleList = SingleList(name_list)

        self.compare_lists(test_list, name_list)

        self.assertIsNone(test_list.tail.next)

    def test_insert_tail(self):
        name:str = "Joe"
        test_list:SingleList = SingleList()

        test_list.insert(name)

        self.assertEqual(test_list.head.name, "Joe")
        self.assertEqual(test_list.tail.name, "Joe")
        self.assertEqual(test_list.tail.next, None)

        test_list.insert("Jack")

        self.assertEqual(test_list.head.name,"Joe")
        self.assertEqual(test_list.head.next.name, "Jack")
        self.assertEqual(test_list.tail.name, "Jack")
        self.assertEqual(test_list.tail.next, None)


    # Test that the constructor is able to create a single node list
    def test_one_name_constructor(self):
        name_list:list = ['Joe']
        test_list:SingleList = SingleList(name_list)

        self.assertEqual(test_list.head.name, name_list[0])
        self.assertEqual(test_list.tail.name, name_list[0])
        self.assertEqual(test_list.head.next, None)
        self.assertEqual(test_list.tail.next, None)

    def test_insert_middle(self):
        name_list:list = ['Joe','Jack','Bill','Sally','George']
        name_list_2:list = ['Joe','Jack','Aaron','Bill','Sally','George']
        test_list:SingleList = SingleList(name_list)

        test_list.insert("Aaron", 2)
        self.compare_lists(test_list, name_list_2)

    def test_insert_front(self):
        name_list:list = ['Joe','Jack','Bill','Sally','George']
        name_list_2:list = ['Aaron','Joe','Jack','Bill','Sally','George']
        test_list:SingleList = SingleList(name_list)

        test_list.insert("Aaron", 0)
        self.compare_lists(test_list, name_list_2)

    def test_insert_one(self):
        name_list:list = ['Joe','Jack','Bill','Sally','George']
        name_list_2:list = ['Joe','Aaron','Jack','Bill','Sally','George']
        test_list:SingleList = SingleList(name_list)

        test_list.insert("Aaron", 1)
        self.compare_lists(test_list, name_list_2)


    def test_remove(self):
        name_list:list = ['Joe','Jack','Aaron','Bill','Sally','George']
        name_list_2:list = ['Joe','Jack','Bill','Sally','George']
        test_list:SingleList = SingleList(name_list)

        rem = test_list.remove("Aaron")
        self.assertEqual(rem, "Aaron")
        self.compare_lists(test_list, name_list_2)

    def test_remove_head(self):
        name_list:list = ['Aaron','Joe','Jack','Bill','Sally','George']
        name_list_2:list = ['Joe','Jack','Bill','Sally','George']
        test_list:SingleList = SingleList(name_list)

        rem = test_list.remove("Aaron")
        self.assertEqual(rem, "Aaron")
        self.compare_lists(test_list, name_list_2)

    def test_remove_tail(self):
        name_list:list = ['Joe','Jack','Bill','Sally','George', 'Aaron']
        name_list_2:list = ['Joe','Jack','Bill','Sally','George']
        test_list:SingleList = SingleList(name_list)

        rem = test_list.remove("Aaron")
        self.assertEqual(rem, "Aaron")
        self.compare_lists(test_list, name_list_2)


if __name__ == '__main__':
    unittest.main()
