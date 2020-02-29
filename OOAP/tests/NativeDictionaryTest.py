import pytest
import random
from NativeD import NativeDictionary

def test_get_empty():
    a = NativeDictionary()
    assert a.get_get_value_status() == a.GET_NONE
    a.get_value('key')
    assert a.get_get_value_status() == a.GET_ERR

def test_get():
    a = NativeDictionary()
    a.put('some_value', 'key')
    assert a.get_value('key') == 'some_value'
    assert a.get_get_value_status() == a.GET_OK

def test_get_wrong():
    a = NativeDictionary()
    a.put('some_value', 'key')
    assert a.get_value(123) == 0
    assert a.get_get_value_status() == a.GET_ERR

def test_remove_empty():
    a = NativeDictionary()
    assert a.get_remove_status() == a.REMOVE_NONE
    a.remove('key')
    assert a.get_remove_status() == a.REMOVE_ERR

def test_remove():
    a = NativeDictionary()
    a.put('value', 'key')
    a.remove('key')
    assert a.get_remove_status() == a.REMOVE_OK
    assert a.get_value('key') == 0
 
def test_in_dict():
    a = NativeDictionary()
    assert a.in_dict('key') == False
    a.put('value', 'key')
    assert a.in_dict('key') == True
    a.remove('key')
    assert a.in_dict('key') == False
