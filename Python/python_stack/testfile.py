# Refer to README.md for the problem instructions


class numNode:
    def __init__(self, num):
        self.num = num
        self.next = None


class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def pushStack(self, items):
        for item in items:
            newNode = numNode(item)
            newNode.next = self.top
            self.top = newNode
            self.size += 1

    def popStack(self, numPops):
        if numPops > self.size:
            return "STACK TOO SMALL"
        else:
            poppedItems = []
            numPopped = 0
            while numPopped != numPops:
                newTop = self.top.next
                poppedItems.append(self.top.num)
                del self.top
                self.top = newTop
                self.size -= 1
                numPopped += 1
            return poppedItems

    def emptyStack(self):
        while self.top.next != None:
            newTop = self.top.next
            del self.top
            self.top = newTop
            self.size -= 1
        self.size = 0
        self.top = None
