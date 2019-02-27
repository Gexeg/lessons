from random import randint

class Heap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_node_index = 0
        self.storage = [None] * capacity

    def add_node(self, value):
        if self.last_node_index == self.capacity:
            return None
        new_node = Node(value)
        current_ind = self.last_node_index
        self.storage[self.last_node_index] = new_node
        self.last_node_index += 1
        while current_ind != 0:
            new_node_value = self.storage[current_ind].value
            parent_node_value = self.storage[(current_ind - 1) // 2].value
            parent_node_index = (current_ind - 1) // 2
            if new_node_value < parent_node_value:
                break
            if new_node_value > parent_node_value:
                self.swap(current_ind, parent_node_index)
            current_ind = parent_node_index

    def pop(self):
        """Получение корня"""
        if self.storage[0]:
            pop = self.storage[0]
        else:
            return None
        self.storage[0] = self.storage[self.last_node_index-1]
        self.storage[self.last_node_index-1] = None
        self.last_node_index -= 1
        current_ind = 0
        while True:
            r_child_index = current_ind * 2 + 2 if current_ind * 2 + 2 < len(self.storage) - 1 else None
            if r_child_index:
                r_child_value = self.storage[r_child_index].value if self.storage[r_child_index] else None
            else:
                r_child_value = None
            l_child_index = current_ind * 2 + 1 if current_ind * 2 + 1 < len(self.storage) - 1 else None
            if l_child_index:
                l_child_value = self.storage[l_child_index].value if self.storage[l_child_index] else None
            else:
                l_child_value = None
            if r_child_value and l_child_value:
               if r_child_value > l_child_value:
                   max_child_ind = r_child_index
                   max_child_value = r_child_value
               else:
                   max_child_ind = l_child_index
                   max_child_value = l_child_value
            elif r_child_value:
                max_child_ind = r_child_index
                max_child_value = r_child_value
            elif l_child_value:
                max_child_ind = l_child_index
                max_child_value = l_child_value
            else:
                return pop
            if self.storage[current_ind].value < max_child_value:
                self.swap(current_ind, max_child_ind)
                current_ind = max_child_ind
            else:
                return pop

    def swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
        return


class Node:
    def __init__(self, value):
        self.value = value

def heap_sort(array):
    heap = Heap(len(array))
    for i in range(len(array)):
        heap.add_node(array.pop())
    while True:
        value = (heap.pop())
        if value is None:
            return
        else:
            array.append(value.value)

array = [randint(0,10) for i in range(10)]
print('Generated array: ', array)
heap_sort(array)
print('Sorted array: ', array)
