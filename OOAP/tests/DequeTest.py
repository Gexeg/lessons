import pytest
from DeQue import Queue, Deque


def test_deque_remove_tail():
    a = Deque()
    for el in range(100):
        a.add_tail(el)
    for i in range(100):
        assert a.get_head() == i 
        assert a.get_head_status() == 1
        a.remove_head()
        assert a.get_remove_head_status() == 1

def test_deque_add_tail():
    a = Deque()
    a.add_tail(12)
    assert a.get_head() == 12
    assert a.get_head_status() == 1
    assert a.get_size() == 1

def test_deque_get_head2():
    a = Deque()
    assert a.get_head_status() == 0
    a.get_head()
    assert a.get_head_status() == 2

def test_queue_add_head():
    a = Queue()
    a.add_head(12)
    assert a.get_tail() == 12
    assert a.get_tail_status() == 1
    assert a.get_size() == 1

def test_queue_get_tail2():
    a = Queue()
    a.get_tail()
    assert a.get_tail_status() == 2

def test_queue_add_head2():
    a = Queue()
    a.add_head(0)
    a.add_head(1)
    a.add_head(0)
    assert a.get_size() == 3
    assert a.get_tail() == 0
    assert a.get_tail_status() == 1

def test_queue_remove_tail():
    a = Queue()
    for el in range(100):
        a.add_head(el)
    for i in range(100):
        assert a.get_tail() == i 
        assert a.get_tail_status() == 1
        a.remove_tail()
        assert a.get_remove_tail_status() == 1

def test_queue_remove_tail2():
    a = Queue()
    a.remove_tail()
    assert a.get_remove_tail_status() == 2
