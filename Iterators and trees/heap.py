import ctypes


class Heap:
    def __init__(self, value):
        self.count = 1
        self.capacity = 15
        self.array = (self.capacity * ctypes.py_object)()
        for i in range(self.capacity):
            self.array[i] = None
        self.array[0] = value

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        return

    def add_node(self, value):
        """Добавление нового узла. Родитель больше ребенка"""
        if self.count == self.capacity:
            return None
        self.array[self.count] = value
        self.count += 1
        current_ind = self.count - 1
        while current_ind != 0:
            if self.array[current_ind] < self.array[(current_ind-1)//2]:
                return
            if self.array[current_ind] > self.array[(current_ind-1)//2]:
                self.swap(current_ind, (current_ind - 1) // 2)
            current_ind = (current_ind-1)//2
        return

    def pop(self):
        """Получение корня"""
        pop = self.array[0]
        self.array[0] = self.array[self.count-1]
        self.array[self.count-1] = None
        current_ind = 0
        while True:
            if current_ind * 2 + 1 < self.capacity and self.array[current_ind] < self.array[current_ind * 2 + 1]:
              self.swap(current_ind, current_ind * 2 + 1)
              current_ind = current_ind * 2 + 1
            elif current_ind * 2 + 2 < self.capacity and self.array[current_ind] < self.array[current_ind * 2 + 2]:
                self.swap(current_ind, current_ind * 2 + 2)
                current_ind = current_ind * 2 + 2
            else:
                return pop


mas_tree = Heap(50)
mas_tree.add_node(25)
mas_tree.add_node(75)
mas_tree.add_node(84)
mas_tree.add_node(62)
mas_tree.add_node(55)
mas_tree.add_node(64)
mas_tree.add_node(92)
mas_tree.add_node(78)
mas_tree.add_node(37)
mas_tree.add_node(31)
mas_tree.add_node(43)
mas_tree.add_node(12)
mas_tree.add_node(15)
mas_tree.add_node(9)

for i in range(mas_tree.capacity):
    print(str(i)+'   '+str(mas_tree.array[i]))

print()

print(mas_tree.pop())

print()

for i in range(mas_tree.capacity):
    print(str(i)+'   '+str(mas_tree.array[i]))
