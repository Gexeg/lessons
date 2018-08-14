import unittest

class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0 , item)

    def removeFront(self):
        return self.queue.pop()

    def removeTail(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

deq = Deque()
deq.addFront("f1")
deq.addTail("t1")
deq.addFront("f2")
deq.addTail("t2")

def check_palindrom(string):
    deq_a = Deque()
    deq_b = Deque()
    for i in string.lower().replace(' ',''):
        deq_a.addFront(i)
        deq_b.addTail(i)
    return deq_a.queue == deq_b.queue


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_check_palindrom(self):
        self.assertEqual( check_palindrom('А Роза упала на лапу Азора'), True)

    def tearDown(self):
        pass

unittest.main()