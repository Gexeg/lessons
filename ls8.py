import ctypes, unittest

class HashTable:

    def __init__(self):
        self.capacity = 19
        self.step = 3
        self.array = (self.capacity*ctypes.py_object)()
        self.full_slots = []

    def hash_fun(self, value):
        return id(value)%19

    def seek_slot(self, value):
        """Метод, находящий свободный слот под значение"""
        slot = self.hash_fun(value)
        if len(self.full_slots)== self.capacity:
            return False
        while slot in self.full_slots:
            slot += self.step
            if slot > self.capacity:
                slot = (slot+4)%3
        return slot

    def put(self, value):
        """Метод, размещающий значение в слоте"""
        if self.seek_slot(value) is not False:
            self.array[self.seek_slot(value)] = value
            self.full_slots.append(self.seek_slot(value))
        return

    def find(self, value):
        """ Метод, выдающий слот в таблице для значения"""
        slot = self.hash_fun(value)
        a = 0
        while slot in self.full_slots:
            if self.array[slot] == value:
                return slot
            slot += self.step
            if slot > self.capacity:
                slot = (slot + 4) % 3
                a +=1
                if a == 3:
                    return False
        return False

h_table = HashTable()
h_table.put('Hash')

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_find(self):
        h_table.put(154)
        self.assertEqual(h_table.find(154), h_table.hash_fun(154))

    def tearDown(self):
        pass

unittest.main()