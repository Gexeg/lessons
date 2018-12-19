class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

