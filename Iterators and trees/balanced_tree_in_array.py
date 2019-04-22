
def GenerateBBSTArray(array):
    sorted_array = sort_array(array)
    builded_tree = create_balanced_tree_in_array(sorted_array)
    return builded_tree.Tree

class aBST:
    def __init__(self, depth):
        self.tree_size = (2 ** (depth + 1)) - 1
        self.Tree = [None] * self.tree_size

    def FindKeyIndex(self, key):
        current_node_index = 0
        while current_node_index < self.tree_size:
            if self.Tree[current_node_index] is None:
                return -current_node_index
            if self.Tree[current_node_index] == key:
                return current_node_index
            elif self.Tree[current_node_index] < key:
                current_node_index = current_node_index * 2 + 2
                if current_node_index not in range(self.tree_size):
                    return None
            elif self.Tree[current_node_index] > key:
                current_node_index = current_node_index * 2 + 1
                if current_node_index not in range(self.tree_size):
                    return None
        return None

    def AddKey(self, key):
        find_result = self.FindKeyIndex(key)
        if find_result == 0:
            self.Tree[0] = key
            return 0
        if find_result is None:
            return -1
        if find_result < 0:
            self.Tree[-find_result] = key
            return -find_result
        if find_result >= 0:
            return -1

def create_balanced_tree_in_array(array):
    """Функция сначала определяет необходимый размер массива и глубину будущего дерева,
    а затем создает корневой элемент и рекурсивно заполняет массив-дерево(TreeInArray)"""
    new_tree_capacity = 0
    tree_depth = 0
    while new_tree_capacity < len(array):
        tree_depth += 1
        new_tree_capacity = (2 ** (tree_depth + 1)) - 1
    new_tree = aBST(tree_depth)
    fill_tree(array, new_tree, 0, len(array) - 1)
    return new_tree

def fill_tree(array, tree, start_index, end_index):
    """Рекурсивная функция, переносит элементы массива в дерево
    (методы у дерева с указателями и дерева в массиве называются одинаково, поэтому она подходит для
    обоих деревьев)"""
    if start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        tree.AddKey(array[middle_index])
        fill_tree(array, tree, start_index, middle_index - 1)
        fill_tree(array, tree, middle_index + 1, end_index)

def sort_array(array):
    """Функция сортирует исходный массив"""
    sorted_array = array
    sorted_array.sort()
    return sorted_array