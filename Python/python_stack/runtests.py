import unittest
from testfile import *
import random

def make_list(size:int):
    return random.sample(range(1, 100), size)

def make_stack(test_list:list):
    myStack = stack()
    myStack.pushStack(test_list)

    return myStack

def make_random_stack(size:int):
    return make_stack(make_list(size))

class CheckRideTestOne(unittest.TestCase):
    def test_pop_empty(self):
        myStack = stack()

        # popping from an empty stack
        self.assertEqual("STACK TOO SMALL", myStack.popStack(2))

    def test_stack(self):
        size = 4
        items = make_list(size)
        mystack = make_stack(items)
        top = mystack.top
        self.assertEqual(mystack.size, size)

        i = 0
        items = items[::-1]
        # step through stack from top to bottom and compare with items
        while top is not None:
            self.assertEqual(top.num, items[i])
            top = top.next
            i += 1 
        # make sure there were 4 items on stack
        self.assertEqual(i, size)

    def test_pop_too_many(self):
        # only 4 items on stack
        self.assertEqual("STACK TOO SMALL", make_random_stack(4).popStack(5))
        

    def test_pop_some(self):
        items = [1, 2, 3, 4]
        myStack = make_stack(items)
        popped = items[:-3:-1]
        # test if the items popped from the stack are the right ones
        self.assertEqual(popped, myStack.popStack(2))
        self.assertEqual(myStack.size, 2)

        top = myStack.top
        items = items[:2][::-1]
        i = 0
        # step through stack from top to bottom and compare with items
        while top is not None:
            self.assertEqual(top.num, items[i])
            top = top.next
            i += 1
        # make sure there were 2 items on stack
        self.assertEqual(i, 2)

    def test_push_more(self):
        items1 = make_list(2)
        items2 = make_list(5)
        myStack = make_stack(items1)
        myStack.pushStack(items2)

        self.assertEqual(myStack.size, 7)
        top = myStack.top

        items = items2[::-1] + items1[::-1]
        i = 0
        # step through stack from top to bottom and compare with items
        while top is not None:
            self.assertEqual(top.num, items[i])
            top = top.next
            i += 1

        self.assertEqual(i, 7)

    def test_empty_stack(self):
        size = 7
        myStack = make_random_stack(size)
        self.assertEqual(myStack.size, size)

        myStack.emptyStack()

        self.assertEqual(myStack.top, None)
        self.assertEqual(myStack.size, 0)

    def test_push_to_empty(self):
        myStack = stack()
        size = 7
        items = make_list(size)
        myStack.pushStack(items)

        top = myStack.top
        items = items[::-1]
        i = 0
        # step through stack from top to bottom and compare with items
        while top is not None:
            self.assertEqual(top.num, items[i])
            top = top.next
            i += 1
        # make sure there were 7 items on stack
        self.assertEqual(i, size)


if __name__ == '__main__':
    unittest.main()
