import unittest


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

    def delete_node(self, key):
        """Удаление узла"""
        if self.root.key == key:
            print('Cannot delete root-node')
            return False
        elif self.find_node(key)[1]:
            node = self.find_node(key)[0]
        else:
            return False
        if node.right_child is None and node.left_child is None:
            if node.parent.right_child and node.parent.right_child.key == key:
                node.parent.right_child = None
                return
            if node.parent.left_child and node.parent.left_child.key == key:
                node.parent.left_child = None
                return
        elif node.right_child is None:
            if node.parent.right_child and node.parent.right_child.key == key:
                node.parent.right_child = node.left_child
                node.left_child.parent = node.parent
                return
            if node.parent.left_child and node.parent.left_child.key == key:
                node.parent.left_child = node.left_child
                node.left_child.parent = node.parent
                return
        else:
            new_node = node.right_child
            while True:
                if new_node.right_child is None and new_node.left_child is None:
                    if node.parent.right_child and node.parent.right_child.key == key:
                        node.parent.right_child = new_node
                        new_node.parent = node.parent
                        return
                    if node.parent.left_child and node.parent.left_child.key == key:
                        node.parent.left_child = None
                        new_node.parent = node.parent
                        return
                new_node = new_node.left_child


a_tree2 = Tree2(14)
a_tree2.add_node(15)
a_tree2.add_node(12)
a_tree2.add_node(18)
a_tree2.add_node(17)
a_tree2.add_node(5464)
a_tree2.add_node(22)
a_tree2.add_node(23)
a_tree2.add_node(21)
a_tree2.add_node(13)


class Ls13Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_min_max_node(self):
        self.assertEqual(a_tree2.min_max_node('min', 14).key, 12)
        self.assertEqual(a_tree2.min_max_node('max', 14).key, 5464)

    def test_delete_node(self):
        a_tree2.delete_node(23)
        self.assertEqual(a_tree2.find_node(23)[1], False)

    def tearDown(self):
        pass


unittest.main()
