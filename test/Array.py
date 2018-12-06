import ctypes, unittest


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, ind, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        if ind >= self.count:
            ind = self.count
        str_ind = self.count
        for i in range(self.count - ind):
            self.array[str_ind]=self.array[str_ind-1]
            str_ind -=1
        self.array[ind]=itm
        self.count +=1
        return

    def delete(self, ind):
        if ind < 0 or ind >= self.count:
            raise IndexError('Index is out of bounds')
        str_ind = ind
        for i in range(self.count - ind -1):
            self.array[str_ind] = self.array[str_ind + 1]
            str_ind += 1
        self.count -= 1
        if self.count <= (self.capacity/2):
            if self.capacity/2 < 16:
                self.resize(16)
            else:
                self.resize(round(self.capacity/1.5))
        return
class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_insert(self):
        da = DynArray()
        capacity_1 = da.capacity
        for i in range(16):
            da.append(i)
        da.insert(2, 151)
        self.assertEqual(da[2], 151)
        self.assertEqual(capacity_1, 16)
        self.assertEqual(da.capacity, 32)

    def test_insert_resize(self):
        da = DynArray()
        for i in range(15):
            da.append(i)
        da.insert(2, 151)
        self.assertEqual(da[2], 151)
        self.assertEqual(da.capacity, 16)

    def test_delete(self):
        da = DynArray()
        for i in range(15):
            da.append(i)
        da.delete(2)
        self.assertEqual(da[2], 3)

    def test_delete_resize(self):
        da = DynArray()
        for i in range(17):
            da.append(i)
        da.delete(15)
        self.assertEqual(da[15], 16)
        self.assertEqual(da.capacity, 21)

    def test_delete_resize_2(self):
        da = DynArray()
        da.capacity = 18
        for i in range(8):
            da.append(i)
        da.delete(6)
        self.assertEqual(da[6], 7)
        self.assertEqual(da.capacity, 16)

    def tearDown(self):
        pass
