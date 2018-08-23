import ctypes, unittest

class HashTable:

    def __init__(self):
        self.capacity = 19
        self.step = 3
        self.slots = (self.capacity * ctypes.py_object)()
        self.values = (self.capacity * ctypes.py_object)()
        self.full_slots = []

    def hash_fun(self, value):
        return id(value)%19

    def seek_slot(self, key):
        """Метод, находящий свободный слот под значение"""
        slot = self.hash_fun(key)
        if len(self.full_slots) == self.capacity:
            return False
        while slot in self.full_slots:
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
        return slot

    def put(self, key, value):
        """Метод, размещающий значение в слотах"""
        if self.seek_slot(key) is not False:
            self.slots[self.seek_slot(key)] = key
            self.values[self.seek_slot(key)] = value
        self.full_slots.append(self.seek_slot(key))
        return



    def is_key(self, key):
        """ Метод, проверяющий есть ли ключ в слотах"""
        slot = self.hash_fun(key)
        a = 0
        while slot in self.full_slots:
            if self.slots[slot] == key:
                return True
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
                a += 1
                if a == self.step:
                    return False
        return False

    def get(self, key):
        """ Метод, выдающий значение по ключу"""
        slot = self.hash_fun(key)
        a = 0
        while slot in self.full_slots:
            if self.slots[slot] == key:
                return self.values[slot]
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
                a += 1
                if a == self.step:
                    return None
        return None

h_table = HashTable()
h_table.put(123, "Hash")
h_table.put(1690, "Hash1")
h_table.put('asdjalks', "Hash2")
h_table.put(390123, "Hash3")

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_key(self):
            self.assertEqual(h_table.is_key(154), False)

    def test_get(self):
        self.assertEqual(h_table.get(123), 'Hash')

    def tearDown(self):
        pass

unittest.main()