import unittest

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        return self.stack.insert(0, value)

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_size_and_peek(self):
        test_stack = Stack()
        test_stack.push(123)
        test_stack.push(456)
        self.assertEqual(test_stack.peek(), 456)
        self.assertEqual(test_stack.size(), 2)

    def test_pop(self):
        test_stack = Stack()
        test_stack.push(123)
        test_stack.push(456)
        self.assertEqual(test_stack.pop(), 456)

    def test_pop_empty_stack(self):
        test_stack = Stack()
        self.assertEqual(test_stack.pop(), None)

    def test_peek(self):
        test_stack = Stack()
        self.assertEqual(test_stack.peek(), None)
        self.assertEqual(test_stack.size(), 0)

    def tearDown(self):
        pass
