import ctypes, unittest


class Tree3:
    def __init__(self, value):
        self.count = 0
        self.capacity = 15
        self.array = (self.capacity * ctypes.py_object)()
        for i in range(self.capacity):
            self.array[i] = None
        self.array[0] = value

    def find_node(self, value):
        """Поиск узла по значению"""
        current_node_index = 0
        for i in range(self.capacity):
            if self.array[current_node_index] == value:
                return current_node_index
            elif self.array[current_node_index] < value:
                current_node_index = current_node_index * 2 + 2
                if current_node_index > self.capacity:
                    return None
                if self.array[current_node_index] is None:
                    return -current_node_index
            elif self.array[current_node_index] > value:
                current_node_index = current_node_index * 2 + 1
                if current_node_index > self.capacity:
                    return None
                if self.array[current_node_index] is None:
                    return -current_node_index
        return None

    def add_node(self, key):
        """Добавление нового узла все, что больше - направо, все, что меньше - налево"""
        find_result = self.find_node(key)
        if find_result is None:
            return False
        if find_result >= 0:
            return False
        if find_result < 0:
            self.array[-find_result] = key
            return


mas_tree = Tree3(50)
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