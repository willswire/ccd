# Refer to README.md for the problem instructions


class queue:
    def __init__(self):
        self.qList = []
        pass

    def enqueue(self, items):
        for item in items:
            self.qList.append(item)
        pass

    def dequeue(self, numRemove):
        if numRemove <= len(self.qList):
            for _ in range(numRemove):
                self.qList.pop(0)
        pass

    def emptyQueue(self):
        for _ in range(len(self.qList)):
            self.qList.pop(0)
        pass

    def peek(self):
        if not self.isEmpty():
            return self.qList[0]
        else:
            return None

    def isEmpty(self):
        return not len(self.qList)

    def size(self):
        return len(self.qList)
