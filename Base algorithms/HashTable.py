import unittest

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return id(value) % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        visited_slots = 0
        while True:
            if self.slots[slot] is None:
                return slot
            slot = (slot + self.step) % self.size
            visited_slots += 1
            if visited_slots > self.size:
                return None

    def put(self, value):
        if self.seek_slot(value) or self.seek_slot(value) == 0:
            free_slot = self.seek_slot(value)
            self.slots[free_slot] = value
            return free_slot
        return None

    def find(self, value):
        slot = self.hash_fun(value)
        marked_slots = 0
        while True:
            if self.slots[slot] == value:
                return slot
            slot = (slot + self.step) % self.size
            marked_slots += 1
            if marked_slots == self.size:
                return None

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_put(self):
        h_table = HashTable(19, 3)
        for i in range(19):
            h_table.put('Hash')
        self.assertEqual(h_table.put('another-hash'), None)

    def test_put_empty_table(self):
        h_table = HashTable(19, 3)
        for i in range(19):
            h_table.put('Hash')

        self.assertEqual(h_table.put('another-hash'), None)

    def test_hash(self):
        h_table = HashTable(19, 3)
        a = h_table.hash_fun('Hash')
        self.assertEqual(a < 20, True)

    def test_find(self):
        h_table = HashTable(100, 3)
        for i in range(100):
            h_table.put('Hash' + str(i))


        a = 0
        for i in range(100):
            if h_table.find('Hash' + str(i)) is None:
                a += 1
        for i in h_table.slots:
            if i is None:
                a +=1
        self.assertEqual(a, 0)

    def tearDown(self):
        pass

unittest.main()