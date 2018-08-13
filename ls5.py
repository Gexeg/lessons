import unittest

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)

def rotate_queue(queue, rotate_turns):
    """Задание 1. Функция вращающая очередь"""
    for i in range(rotate_turns):
        queue.enqueue(queue.dequeue())
    return queue.items

class Stack:
    """Стек работает с первыми элементами списка, а не с последними"""
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        return self.stack.insert(0, value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]

    def size(self):
        return len(self.stack)

class Stack_queue:
    """Задание 2. Очередь, реализованная с помощью 2 стеков"""
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def enqueue(self, value):
        return self.stack_a.push(value)

    def dequeue(self):
        if self.stack_a.size() == 0:
            return None
        for i in range(self.stack_a.size() - 1):
            self.stack_b.push(self.stack_a.pop())
        item = self.stack_a.pop()
        while self.stack_b.size() > 0:
            self.stack_a.push(self.stack_b.pop())
        return item

    def size(self):
        return len(self.stack_a)

test_queue = Stack_queue()
test_queue.enqueue(2)
test_queue.enqueue(3)
test_queue.enqueue(5)
test_queue.enqueue(10)


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_rotate_queue(self):
        self.assertEqual(rotate_queue(qu, 2), [2,1,3])

    def test_stack_queue(self):
        self.assertEqual(test_queue.dequeue(), 2)

    def tearDown(self):
        pass

unittest.main()
