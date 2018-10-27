import ctypes, random, timeit


class Tree2Node:
    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key
        self.depth = None
        self.have_hollow = False


class TreeWithPointers:
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


class TreeInArray:
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
                if current_node_index not in range(self.capacity):
                    return None
                if self.array[current_node_index] is None:
                    return -current_node_index
            elif self.array[current_node_index] > value:
                current_node_index = current_node_index * 2 + 1
                if current_node_index not in range(self.capacity):
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


"""новый код расположен после коммента"""

def sort_array(array):
    """Функция сортирует исходный массив"""
    sorted_array = array
    sorted_array.sort()
    return sorted_array


def fill_tree(array, tree, start_index, end_index):
    """Рекурсивная функция, переносит элементы массива в дерево
    (методы у дерева с указателями и дерева в массиве называются одинаково, поэтому она подходит для
    обоих деревьев)"""
    if start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        tree.add_node(array[middle_index])
        fill_tree(array, tree, start_index, middle_index - 1)
        fill_tree(array, tree, middle_index + 1, end_index)


def create_balanced_tree_in_array(array):
    """Функция сначала определяет необходимый размер массива и глубину будущего дерева,
    а затем создает корневой элемент и рекурсивно заполняет массив-дерево(TreeInArray)"""
    new_tree_capacity = 0
    tree_depth = 0
    while new_tree_capacity < len(array):
        tree_depth += 1
        new_tree_capacity = (2 ** (tree_depth + 1)) - 1
    middle = len(array) // 2
    new_tree = TreeInArray(new_tree_capacity, array[middle])
    fill_tree(array, new_tree, 0, middle - 1)
    fill_tree(array, new_tree, middle + 1, len(array) - 1)
    return new_tree


def create_balanced_tree_with_pointers(array):
    """Функция строит дерево на основе класса TreeWithPointers"""
    middle = len(array) // 2
    new_tree = TreeWithPointers(array[middle])
    fill_tree(array, new_tree, 0, middle - 1)
    fill_tree(array, new_tree, middle + 1, len(array) - 1)
    return new_tree


def check_is_bynary(tree):
    """Тестовая функция для дерева с указателями. Проходит дерево в глубину и проставляет характеристику "глубина узла"
    так же проверяет правильно ли расставлены дети для текущего узла"""
    stack = []
    current_node = tree.root
    current_node.depth = 1
    stack.append(current_node)
    current_node = stack.pop()
    if current_node.right_child:
        if current_node.right_child.key < current_node.key:
            return False
        stack.append(current_node.right_child)
    if current_node.left_child:
        if current_node.left_child.key > current_node.key:
            return False
        stack.append(current_node.left_child)
    while len(stack) > 0:
        current_node = stack.pop()
        current_node.depth = current_node.parent.depth + 1
        if current_node.right_child:
            if current_node.right_child.key < current_node.key:
                return False
            stack.append(current_node.right_child)
        if current_node.left_child:
            if current_node.left_child.key > current_node.key:
                return False
            stack.append(current_node.left_child)
    return True


def measure_depth_if_balanced(node):
    """Тестовая функция для дерева с указателями. Рекурсивно проверяет сбалансированно ли дерево
    Если да, то возвращает его глубину"""
    if node is None:
        return 0
    left_depth = measure_depth_if_balanced(node.left_child)
    if left_depth == -1:
        return -1
    right_depth = measure_depth_if_balanced(node.right_child)
    if right_depth == -1:
        return -1
    if abs(left_depth - right_depth) > 1:
        return -1
    return max(left_depth, right_depth) + 1


def check_is_balanced(tree):
    """Тестовая функция связка с measure_depth_if_balanced. Возвращает true/false, в зависимости от ответа первой
    функции"""
    root_node = tree.root
    return measure_depth_if_balanced(root_node) >= 0

test_array_for_bst_with_pointers = [random.random()*100 for i in range(10000)]
test_array_for_array_bst = [random.random()*100 for i in range(10000)]

bst_with_pointers = create_balanced_tree_with_pointers(sort_array(test_array_for_bst_with_pointers))

bst_in_array = create_balanced_tree_in_array(sort_array(test_array_for_array_bst))

t1 = timeit.Timer(lambda: create_balanced_tree_in_array(sort_array(test_array_for_array_bst))).timeit(number=1)
t2 = timeit.Timer(lambda: create_balanced_tree_with_pointers(sort_array(test_array_for_bst_with_pointers))).timeit(number=1)

print('Create tree in array: ', t1)
print()
print('Create tree with pointers: ', t2)
print('Tree is binary: ', check_is_bynary(bst_with_pointers))
print('Tree is balanced:', check_is_balanced(bst_with_pointers))