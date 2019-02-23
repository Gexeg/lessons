import random, timeit

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

mas_tree = Heap(5)
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
    value = mas_tree.storage[i].value if mas_tree.storage[i] else 'None'
    print(str(i)+'   '+str(value))

print()

print(mas_tree.pop().value)

print()

for i in range(mas_tree.capacity):
    value = mas_tree.storage[i].value if mas_tree.storage[i] else 'None'
    print(str(i)+'   '+str(value))