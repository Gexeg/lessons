import pytest
from Queue import Queue

def test_enqueue():
    a = Queue()
    a.enqueue(12)
    assert a.get_value() == 12
    assert a.get_value_status() == 1
    assert a.get_size() == 1

def test_get_value2():
    a = Queue()
    a.get_value()
    assert a.get_value_status() == 2

def test_enqueue2():
    a = Queue()
    a.enqueue(0)
    a.enqueue(1)
    a.enqueue(0)
    assert a.get_size() == 3
    assert a.get_value() == 0
    assert a.get_value_status() == 1

def test_dequeue():
    a = Queue()
    for el in range(100):
        a.enqueue(el)
    for i in range(100):
        assert a.get_value() == i 
        assert a.get_value_status() == 1
        a.dequeue()
        assert a.get_dequeue_status() == 1

def test_dequeue2():
    a = Queue()
    a.dequeue()
    assert a.get_dequeue_status() == 2
