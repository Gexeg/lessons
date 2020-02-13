import pytest
from DynArray import DynArray

def test_append():
    a = DynArray()
    a.append(1)
    assert a.get_value(0) == 1
    a.append(2)
    assert a.get_value(0) == 1
    assert a.get_value(1) == 2

def test_insert():
    a = DynArray()
    for i in range(10):
        a.append(i)
    a.insert(155, 5)
    assert a.get_insert_status() == 1
    assert a.get_value(5) == 155
    assert a.get_value(10) == 9

    a.insert(200, 150)
    assert a.get_insert_status() == 2

def test_remove():
    a = DynArray()
    for i in range(10):
        a.append(i)
    a.remove(5)
    assert a.get_value(5) == 6
    assert a.get_remove_status() == 1

    a.remove(15)
    assert a.get_remove_status() == 2

def test_size():
    a = DynArray()
    for i in range(10):
        a.append(i)
    assert a.get_size() == 10



