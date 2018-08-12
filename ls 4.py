import unittest

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

stack = Stack()
stack.push(1)
stack.push("2")
stack.push(3.14)

def check_brackets(str):
    """Функция для проверки правильной расстановки скобок"""
    st = Stack()
    for s in str:
        if s == ')':
            if st.size() == 0:
                return False
            st.pop()
        if s =='(':
            st.push('(')
    if st.size() == 0:
        return True
    else:
        return False

def lt_math():
    """Решение примера с постфиксной записью"""
    samp = Stack()
    samp.push('=')
    samp.push('+')
    samp.push(9)
    samp.push('*')
    samp.push(5)
    samp.push('+')
    samp.push(2)
    samp.push(8)
    dec = Stack()
    while samp.size() > 0:
        if type(samp.peak()) == int or type(samp.peak()) == float:
            dec.push(samp.pop())

        elif type(samp.peak()) != int or type(samp.peak()) != float:
            if samp.peak() == '+':
                samp.pop()
                dec.push(dec.pop() + dec.pop())
            elif samp.peak() == '*':
                samp.pop()
                dec.push(dec.pop() * dec.pop())
            elif samp.peak() == '=':
                print(dec.stack)
                return dec.pop()
    return False

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_check_brackets(self):
        self.assertEqual(check_brackets('()()()()'), True)

    def test_lt_math(self):
        self.assertEqual(lt_math(), 59)

    def tearDown(self):
        pass

unittest.main()