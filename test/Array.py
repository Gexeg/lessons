import ctypes


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
        if ind < 0 or ind >= self.count:
            raise IndexError('Index is out of bounds')
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
