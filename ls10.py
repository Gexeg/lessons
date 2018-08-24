import ctypes, unittest


class PowerSet:

    def __init__(self):
        self.capacity = 19
        self.step = 3
        self.array = (self.capacity*ctypes.py_object)()
        self.full_slots = []

    def hash_fun(self, value):
        return id(value) % 19

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        if len(self.full_slots) == self.capacity:
            return False
        while slot in self.full_slots:
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
        return slot

    def find(self, value):
        slot = self.hash_fun(value)
        a = 0
        while slot in self.full_slots:
            if self.array[slot] == value:
                return slot
            slot += self.step
            if slot >= self.capacity:
                slot = (slot + 1) % self.step
                a += 1
                if a == 3:
                    return False
        return False

    def put(self, value):
        if self.find(value) is False:
            if self.seek_slot(value):
                self.array[self.seek_slot(value)] = value
                self.full_slots.append(self.seek_slot(value))
        return

    def remove(self, value):
        self.full_slots.remove(self.find(value))
        return

    def intersection(self, another_set):
        result = PowerSet()
        try:
            for i in self.full_slots:
                for y in another_set.full_slots:
                    if self.array[i] == another_set.array[y]:
                        result.put(self.array[i])
        except:
            return False
        else:
            return result

    def union(self, another_set):
        result = PowerSet()
        try:
            for i in self.full_slots:
                result.put(self.array[i])
            for i in another_set.full_slots:
                result.put(another_set.array[i])
        except:
            return False
        else:
            return result

    def difference(self, another_set):
        result = PowerSet()
        try:
            for i in self.full_slots:
                if another_set.find(self.array[i]) is False:
                    result.put(self.array[i])
        except:
            return False
        else:
            return result

    def issubset(self, another_set):
        try:
            a = 0
            for y in another_set.full_slots:
                for i in self.full_slots:
                    if self.array[i] == another_set.array[y]:
                        a +=1
            if a == len(another_set.full_slots):
                return True
        except:
            return False
        else:
            return False

h_set = PowerSet()
h_set.put("Hash")
h_set.put('123')
h_set.put('9')


a_set = PowerSet()
a_set.put('Hash')

c_set = PowerSet()
c_set.put('Hash')
c_set.put('1978')


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_put_and_remove(self):
            h_set.put(154)
            h_set.put(154)
            h_set.remove(154)
            self.assertEqual(h_set.find(154), False)

    def test_isssubset(self):
        self.assertEqual(h_set.issubset(a_set), True)

    def test_intersection(self):
        test = h_set.intersection(a_set)
        self.assertEqual(test.array[test.find('Hash')], 'Hash')
        self.assertEqual(test.find('123'), False)

    def test_difference(self):
        test = h_set.difference(a_set)
        self.assertEqual(test.array[test.find('123')], '123')
        self.assertEqual(test.array[test.find('9')], '9')

    def test_union(self):
        test = h_set.union(c_set)
        test.remove("Hash")
        self.assertEqual(test.find('Hash'), False)
        self.assertEqual(test.array[test.find('9')], '9')

    def tearDown(self):
        pass

unittest.main()
