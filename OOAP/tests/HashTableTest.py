import pytest
import random
from HashTable import HashTable

def test_full():
    for cap in range(1000):
        a = HashTable(cap)
        assert a.get_put_status() == 0
        for _ in range(cap):
            a.put(random.randint(0, 101010))
            assert a.get_put_status() == 1
        assert a.get_size() == a.get_max_size()
        a.put(155)
        assert a.get_put_status() == 2


def test_in_table():
    for cap in range(1000):
        a = HashTable(cap)
        values = []
        for _ in range(cap):
            value = random.randint(0, 101010)
            a.put(value)
            values.append(value)
        
        random.shuffle(values)
        for el in values:
            assert a.in_table(el) is True

def test_remove():
    for cap in range(1000):
        a = HashTable(cap)
        
        assert a.get_remove_status() == 0
        a.remove(10)
        assert a.get_remove_status() == 2

        values = []
        for el in range(cap):
            a.put(el)
            values.append(el)
        
        random.shuffle(values)
        for el in values:
            a.remove(el)
            assert a.get_remove_status() == 1
            assert a.in_table(el) is False
