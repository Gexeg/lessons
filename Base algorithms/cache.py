import ctypes, unittest

class HashTable:

    def __init__(self):
        self.capacity = 19
        self.step = 3
        self.slots = (self.capacity * ctypes.py_object)()
        self.values = (self.capacity * ctypes.py_object)()
        self.hits = (self.capacity * ctypes.py_object)()
        self.full_slots = []

    def hash_fun(self, value):
        if id(value) % 19 == 0:
            return None
        return id(value) % 19

    def seek_slot(self, key):
        if len(self.full_slots) == self.capacity:
            hits = []
            for i in self.hits:
                hits.append(i)
            ind = hits.index(min(hits))
            self.full_slots.remove(ind)
            return ind
        if  self.hash_fun(key) is None:
            slot = 0
        else:
            slot = self.hash_fun(key)
        while slot in self.full_slots:
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
        if slot == 0:
            return None
        else:
            return slot

    def put(self, key, value):
        slot = self.seek_slot(key)
        if slot is None:
            self.slots[0] = key
            self.values[0] = value
            self.hits[0] = 0
            self.full_slots.append(0)
            return
        elif slot is not False:
            self.slots[slot] = key
            self.values[slot] = value
            self.hits[slot] = 0
            self.full_slots.append(slot)
            return



    def is_key(self, key):
        if  self.hash_fun(key) is None:
            slot = 0
        else:
            slot = self.hash_fun(key)
        a = 0
        while slot in self.full_slots:
            if self.slots[slot] == key:
                self.hits[slot] = self.hits[slot] + 1
                return True
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
                a += 1
                if a == self.step:
                    return False
        return False

    def get(self, key):
        if  self.hash_fun(key) is None:
            slot = 0
        else:
            slot = self.hash_fun(key)
        a = 0
        while slot in self.full_slots:
            if self.slots[slot] == key:
                self.hits[slot] = self.hits[slot] + 1
                return self.values[slot]
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
                a += 1
                if a == self.step:
                    return None
        return None

h_table = HashTable()

for i in range(h_table.capacity):
    h_table.put(i, 'Hash'+str(i))

for i in range(h_table.capacity-1):
    h_table.is_key(i)
    h_table.get(i)

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_put(self):
        h_table.put(154, 'Test')
        self.assertEqual(h_table.get(154), 'Test')
        self.assertEqual(h_table.get(18), None)

    def tearDown(self):
        pass

unittest.main()

