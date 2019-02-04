import unittest


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

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_dequeue(self):
        a = Queue()
        a.enqueue('c')
        a.enqueue('B')
        a.enqueue('B')
        a.enqueue('B')
        a.enqueue('B')
        a.enqueue('B')
        self.assertEqual(a.dequeue(),'c')

    def test_dequeue_empty(self):
        a = Queue()
        self.assertEqual(a.dequeue(), None)


    def test_size(self):
        a = Queue()
        a.enqueue('c')
        a.enqueue('B')
        self.assertEqual(a.size(), 2)
        
    def tearDown(self):
        pass