import unittest


class Stack:
    """Стек работает с первыми элементами списка, а не с последними"""

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class TreeNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.child = []
        self.value = value
        if parent == None:
            self.level = 0
        else:
            self.level = parent.level + 1


class SimpleTree:
    def __init__(self, root):
        self.root = TreeNode(None, root)
        self.current = self.root
        self.node_stack = Stack()
        self.node_stack.push(self.root)

    def reload(self):
        """ Метод для перезапуска итератора"""
        while self.node_stack.size() != 0:
            self.node_stack.pop()
        self.node_stack.push(self.root)
        return

    def __iter__(self):
        return self

    def __next__(self):
        if self.node_stack.size() == 0:
            raise StopIteration
        else:
            node = self.node_stack.pop()
            for element in node.child:
                self.node_stack.push(element)
        return node

    def add_tree_node(self, value):
        """Добавление дочернего узла к текущему узлу"""
        new_node = TreeNode(self.current, value)
        self.current.child.append(new_node)
        self.current = new_node
        return

    def delete_node(self):
        """Удаление текущего узла"""
        if self.current == self.root:
            print('Cannot delete root node.')
            return False
        for i in self.current.child:
            i.parent = self.current.parent
        self.current.parent.child.extend(self.current.child)
        self.current.parent.child.remove(self.current)
        self.current = self.current.parent
        return

    def find_nodes(self, value):
        """Поиск всех злов по значению"""
        result = []
        for i in iter(self):
            if i.value == value:
                result.append(i)
        return result

    def move_node(self, node_value, new_parent):
        """Перемещение узла дочерним к новому родителю"""
        if node_value == self.root.value:
            print('Cannot move root node')
            return False
        child_node = None
        new_parent_node = None
        looking_for_child = True
        looking_for_parent = True
        for i in iter(self):
            if i.value == node_value and looking_for_child:
                child_node = i
                looking_for_child = False
            elif i.value == new_parent and looking_for_parent:
                new_parent_node = i
                looking_for_parent = False
        if looking_for_child is False and looking_for_parent is False:
            child_node.parent.child.remove(child_node)
            for i in child_node.child:
                i.parent = child_node.parent
                child_node.parent.child.append(i)
                child_node.child.remove(i)
            new_parent_node.child.append(child_node)
            child_node.parent = new_parent_node
        return

    def count_nodes_and_leafs(self):
        """Сосчитать все узлы и отдельно только листья"""
        nodes = []
        leafs = []
        for i in iter(self):
            nodes.append(i)
            if len(i.child) == 0:
                leafs.append(i)
        return len(nodes), len(leafs)


a_tree = SimpleTree(15)
a_tree.add_tree_node(13)
a_tree.add_tree_node(19)
a_tree.add_tree_node(111)
a_tree.add_tree_node(157)
a_tree.add_tree_node(15)

a_tree.current = a_tree.current.parent.parent

a_tree.add_tree_node(1768)
a_tree.add_tree_node(1890)

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_count_nodes(self):
        a_tree.reload()
        self.assertEqual(a_tree.count_nodes_and_leafs(), (8, 2))

    def test_find(self):
        a_tree.reload()
        self.assertEqual(a_tree.find_nodes(15)[0].value, 15)

    def test_move_node(self):
        a_tree.reload()
        self.assertEqual(a_tree.find_nodes(19)[0].parent.value, 13)
        a_tree.reload()
        a_tree.move_node(19, 1768)
        a_tree.reload()
        self.assertEqual(a_tree.find_nodes(19)[0].parent.value, 1768)

    def test_del(self):
        a_tree.reload()
        current = a_tree.current
        a_tree.delete_node()
        self.assertEqual(len(a_tree.find_nodes(current.value)), 0)

    def tearDown(self):
        pass


unittest.main()