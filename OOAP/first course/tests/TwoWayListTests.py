import pytest
from TwoWayList import LinkedList, TwoWayList

def test_cursor_moves():
    s_list = LinkedList()
    s_list.add_tail(125)
    s_list.add_tail(135)
    s_list.add_tail(150)
    s_list.head()
    assert s_list.is_head()
    assert s_list.get() == 125
    s_list.right()
    assert s_list.get_right_status() == 1
    assert s_list.get() == 135
    s_list.tail()
    assert s_list.is_tail()
    assert s_list.get() == 150

def test_remove_all():
    s_list = LinkedList()
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.head()
    s_list.remove_all(125)
    s_list.find(125)
    assert s_list.get_find_status() == 2
    assert s_list.size() == 0
    assert s_list._tail == None
    assert s_list._head == None

def test_remove_all_s_in_one_element_list():
    s_list = LinkedList()
    s_list.add_tail(125)
    s_list.remove_all(125)
    s_list.find(125)
    assert s_list.get_find_status() == 2
    assert s_list.size() == 0
    assert s_list._tail == None
    assert s_list._head == None

def test_remove_all_various_s():
    s_list = LinkedList()
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.add_tail(45)
    s_list.add_tail(165)
    s_list.add_tail(155)
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.add_tail(12)
    s_list.add_tail(125)
    s_list.add_tail(125)
    s_list.remove_all(125)

    s_list.find(125)
    assert s_list.get_find_status() == 2
    s_list.head() 
    assert s_list.get() == 45
    s_list.tail()
    assert s_list.get() == 12

def test_remove_all_various_s_one_head():
    s_list = LinkedList()
    s_list.add_tail((175))
    s_list.add_tail((125))
    s_list.remove_all(125)
    s_list.find(125)
    assert s_list.get_find_status() == 2
    s_list.head() 
    assert s_list.get() == 175
    s_list.tail()
    assert s_list.get() == 175

def test_remove():
    s_list = LinkedList()
    s_list.add_tail((175))
    s_list.remove()
    s_list.find(175)
    assert s_list.get_find_status() == 2
    s_list.head()
    assert s_list.is_head() == False
    s_list.tail()
    assert s_list.is_tail() == False
    assert s_list.is_value() == False

def test_delete_():
    s_list = LinkedList()
    s_list.add_tail((175))
    s_list.add_tail((175))
    s_list.add_tail((175))
    s_list.add_tail((175))
    s_list.remove()
    assert s_list.size() == 3
    s_list.head() 
    assert s_list.get() == 175
    s_list.tail()
    assert s_list.get() == 175

def test_remove_empty_list():
    s_list = LinkedList()
    s_list.remove()
    assert s_list.get_remove_status() == 2

def test_find_one_element():
    s_list = LinkedList()
    s_list.add_tail((125))
    s_list.find(125)
    assert s_list.get_find_status() == 2

def test_find():
    s_list = LinkedList()
    s_list.add_tail((125))
    s_list.add_tail((125))
    s_list.find(125)
    assert s_list.get_find_status() == 1

def test_find_none():
    s_list = LinkedList()
    s_list.find(125)
    assert s_list.get_find_status() == 2


def test_put_right():
    s_list = LinkedList()
    s_list.add_tail(175)
    for el in range(10):
        s_list.put_right(el)

    s_list.head()
    assert s_list.get() == 175
    s_list.tail()
    assert s_list.get() == 0
    assert s_list.size() == 11


def test_put_left():
    s_list = TwoWayList()
    s_list.add_tail(175)
    for el in range(10):
        s_list.put_left(el)

    s_list.tail()
    for _ in range(s_list.size() - 1):
        s_list.left()
        assert s_list.get_left_status() == 1
    s_list.head()
    assert s_list.get() == 0
    s_list.tail()
    assert s_list.get() == 175
    assert s_list.size() == 11


def test_put_empty_list():
    s_list = LinkedList()
    s_list.put_right(5)
    assert s_list.get_put_status() == 2
    s_list.put_left(5)
    assert s_list.get_put_status() == 2
