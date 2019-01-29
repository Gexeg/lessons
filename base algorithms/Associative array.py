import unittest

class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
         slot = id(str(key)) % self.size
         marked_slots = 0
         while True:
             if self.slots[slot] is None or self.slots[slot] == key:
                 return slot
             slot = (slot + 1) % self.size
             marked_slots += 1
             if marked_slots > self.size:
                 return None

    def is_key(self, key):
         slot = self.hash_fun(key)
         marked_slots = 0
         if slot:
             while True:
                 if self.slots[slot] == key:
                     return True
                 slot = (slot + 1) % self.size
                 marked_slots += 1
                 if marked_slots == self.size:
                     return False

    def put(self, key, value):
         slot = self.hash_fun(key)
         if slot or slot == 0:
             self.slots[slot] = key
             self.values[slot] = value
         return

    def get(self, key):
         if self.is_key(key):
             slot = self.hash_fun(key)
             marked_slots = 0
             while True:
                 if self.slots[slot] == key:
                     return self.values[slot]
                 slot = (slot + 1) % self.size
                 marked_slots += 1
                 if marked_slots > self.size:
                     return None
         return None

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_real_key(self):
        h_table = NativeDictionary(19)
        for i in range(19):
            h_table.put(i, 'Hello' + str(i))
        self.assertEqual(h_table.get(5), 'Hello5')

    def test_get_false_key(self):
        h_table = NativeDictionary(19)
        for i in range(19):
            h_table.put(i, 'Hello' + str(i))
        self.assertEqual(h_table.get(20), None)

    def test_put_replace(self):
        h_table = NativeDictionary(19)
        for i in range(19):
            h_table.put(i, 'Hello')
        h_table.put(5, 'World')
        self.assertEqual(h_table.get(5), 'World')

    def test_is_key(self):
        h_table = NativeDictionary(19)
        for i in range(19):
            h_table.put(i, 'Hello')
        test_counter = 0
        for i in range(19):
            if h_table.is_key(i) is False:
                test_counter +=1
        self.assertEqual(test_counter, 0)

    def test_is_key_false(self):
        h_table = NativeDictionary(19)
        self.assertEqual(h_table.is_key('25'), False)

    def tearDown(self):
        pass
