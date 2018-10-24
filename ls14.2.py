import ctypes

class Tree2Node:
    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key


class Tree2:
    def __init__(self, key):
        self.root = Tree2Node(None, key)

    def find_node(self, value):
        """Поиск узла по значению"""
        current_node = self.root
        finded = False
        lr_child = None
        while True:
            if current_node.key == value:
                finded = True
                return current_node, finded, lr_child
            elif current_node.key < value:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    lr_child = 'right'
                    return current_node, finded, lr_child
            elif current_node.key > value:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    lr_child = 'left'
                    return current_node, finded, lr_child

    def add_node(self, key):
        """Добавление нового узла все, что больше - направо, все, что меньше - налево"""
        find_result = self.find_node(key)
        if find_result[1]:
            print('No duplicates allowed')
            return False
        if find_result[1] is False:
            if find_result[2] == 'right':
                find_result[0].right_child = Tree2Node(find_result[0], key)
                return
            elif find_result[2] == 'left':
                find_result[0].left_child = Tree2Node(find_result[0], key)
                return

    def min_max_node(self, mm, start_node):
        """Метод поиска максимального/минимального значения в дереве"""
        node = self.find_node(start_node)[0]
        if mm == 'min':
            while True:
                if node.left_child:
                    node = node.left_child
                else:
                    return node
        if mm == 'max':
            while True:
                if node.right_child:
                    node = node.right_child
                else:
                    return node


class Tree3:
    def __init__(self, capacity, value):
        self.capacity = capacity
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

def fill_tree(array, tree, start_index, end_index):
    if start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        tree.add_node(array[middle_index])
        fill_tree(array, tree, start_index, middle_index - 1)
        fill_tree(array, tree, middle_index + 1, end_index)


def create_balanced_tree(array):
    middle = len(array)//2
    new_tree = Tree3(len(array)*2,array[middle])
    fill_tree(array, new_tree, 0, middle - 1)
    fill_tree(array, new_tree, middle + 1, len(array) -1)
    return new_tree


test_array = [1,2,3,4,5,6,7,8,9,10]

c = create_balanced_tree(test_array)

print()
for i in range(c.capacity):
    print(c.array[i],'-',i,)
