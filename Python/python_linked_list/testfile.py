from typing import Iterable
from myNode import Node
# Refer to README.md for the problem instructions


class SingleList():
    def __init__(self, name_list: Iterable = None) -> None:
        if name_list == None:
            self.head = None
            self.tail = None
        else:
            self.head = Node(name_list[0])
            self.tail = self.head
            for index in range(1, len(name_list)):
                newNode = Node(name_list[index])
                currentNode = self.head
                while (currentNode.next != None):
                    currentNode = currentNode.next
                currentNode.next = newNode
                if (index == len(name_list) - 1):
                    self.tail = newNode
        pass

    def remove(self, name: str) -> str or None:
        if self.head.name == name:
            temp = self.head.next
            del self.head
            self.head = temp
            return name
        else:
            currentNode = self.head
            while (currentNode.next != None):
                nextNode = currentNode.next
                if (nextNode.name == name):
                    newNextNode = nextNode.next
                    del nextNode
                    currentNode.next = newNextNode
                    return name
                currentNode = nextNode
        return None

    def insert(self, name: str, position: int = None):
        if (position == None):
            newNode = Node(name)
            if (self.head == None):
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = self.tail.next
        elif (position == 0):
            newNode = Node(name)
            newNode.next = self.head
            self.head = newNode
            pass
        else:
            newNode = Node(name)
            index = 0
            currentNode = self.head
            while (index < (position - 1) and currentNode.next != None):
                currentNode = currentNode.next
                index += 1
            temp = currentNode.next
            currentNode.next = newNode
            newNode.next = temp
            pass