import unittest


class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0, item)

    def removeFront(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop()

    def removeTail(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_dequeue(self):
        a = Deque()
        a.addFront('c')
        a.addFront('D')
        a.addFront('B')
        self.assertEqual(a.removeTail(), 'c')
        self.assertEqual(a.removeFront(), 'B')

    def test_addTail(self):
        a = Deque()
        a.addFront('c')
        a.addFront('B')
        a.addTail('B')
        self.assertEqual(a.removeTail(), 'B')
        self.assertEqual(a.removeFront(), 'B')
        self.assertEqual(a.size(), 1)

    def test_addTail_2(self):
        a = Deque()
        a.addTail('c')
        a.addTail('B')
        a.addTail('B')
        self.assertEqual(a.removeTail(), 'B')
        self.assertEqual(a.removeFront(), 'c')

    def test_remove_empty(self):
        a = Deque()
        a.addTail('c')
        self.assertEqual(a.removeFront(), 'c')
        self.assertEqual(a.removeFront(), None)
        self.assertEqual(a.removeTail(), None)

    def test_remove_empty_2(self):
        a = Deque()
        self.assertEqual(a.removeFront(), None)
        self.assertEqual(a.removeTail(), None)

    def tearDown(self):
        pass