class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла

class BalancedBST:

    def __init__(self):
        self.Root = None
        self.BSTArray = []  # временный массив для ключей дерева

    def CreateFromArray(self, array):
        """Метод сортирует массив, определяет необходимый размер массива для структуры дерева,
        а затем  рекурсивно заполняет массив-дерево(BST_array)"""
        sorted_array = array
        sorted_array.sort()
        new_tree_capacity = 0
        tree_depth = 0
        while new_tree_capacity < len(array):
            tree_depth += 1
            new_tree_capacity = (2 ** (tree_depth + 1)) - 1
        self.BSTArray = [None] * new_tree_capacity
        self.fill_bst_array(array, 0, len(array) - 1, 0)

    def fill_bst_array(self, array, array_start_index, array_end_index, node_index):
        """Рекурсивный метод, выстраивает структуру сбалансированного дерева поиска в массиве"""
        if array_start_index <= array_end_index:
            middle_index = (array_start_index + array_end_index) // 2
            self.BSTArray[node_index] = array[middle_index]
            self.fill_bst_array(array, array_start_index, middle_index - 1, node_index * 2 + 1)
            self.fill_bst_array(array, middle_index + 1, array_end_index, node_index * 2 + 2)

    def GenerateTree(self):
        self.Root = self.build_tree(0)

    def build_tree(self, index, parent=None):
        """Метод строит дерево с указателями из массива. Предполагается, что массив
        содержит структуру сбалансированного двоичного дерева"""
        if index < len(self.BSTArray):
            root = BSTNode(self.BSTArray[index], parent)
            if parent:
                root.Level = parent.Level + 1
            else:
                root.Level = 1
            root.LeftChild = self.build_tree(index*2+1, root)
            root.RightChild = self.build_tree(index*2+2, root)
            return root
        return None

    def IsBalanced(self, root_node):
        """Тестовый метод-связка с measure_depth_if_balanced.
        Возвращает true/false, в зависимости от ответа первого метода"""
        if self.check_is_bynary(root_node):
            return self.measure_depth_if_balanced(root_node) >= 0
        return False

    def check_is_bynary(self, root_node):
        """Тестовый метод, который проходит дерево в глубину
        и проверяет правильно ли расставлены дети для текущего узла"""
        stack = [root_node]
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.RightChild:
                if current_node.RightChild.NodeKey < current_node.NodeKey:
                    return False
                stack.append(current_node.RightChild)
            if current_node.LeftChild:
                if current_node.LeftChild.NodeKey > current_node.NodeKey:
                    return False
                stack.append(current_node.LeftChild)
        return True

    def measure_depth_if_balanced(self, node):
        """Тестовый метод, который рекурсивно проверяет сбалансированно ли дерево
        Если да, то возвращает его глубину"""
        if node is None:
            return 0
        left_depth = self.measure_depth_if_balanced(node.LeftChild)
        if left_depth == -1:
            return -1
        right_depth = self.measure_depth_if_balanced(node.RightChild)
        if right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1
