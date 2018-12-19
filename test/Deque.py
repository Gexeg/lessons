class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0, item)

    def removeFront(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def removeTail(self):
        if len(self.items) == 0:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)
