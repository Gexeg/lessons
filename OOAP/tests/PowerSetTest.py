from PowerSet import PowerSet

def test_put():
    a = PowerSet(16)
    assert a.get_put_status() == a.PUT_NONE
    a.put(15)
    assert a.get_put_status() == a.PUT_OK
    assert a.in_table(15) == True
    a.put(15)
    assert a.get_put_status() == a.PUT_ERR
    a.remove(15)
    assert a.in_table(15) == False
