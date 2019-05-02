import unittest

class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None
        self.node_stack = []
        self.node_stack.append(self.Root)

    def __iter__(self):
        if self.Root is None:
            raise StopIteration
        self.node_stack.clear()
        self.node_stack.append(self.Root)
        return self

    def __next__(self):
        if len(self.node_stack) == 0:
            raise StopIteration
        else:
            node = self.node_stack.pop()
            for child in node.Children:
                self.node_stack.append(child)
        return node

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if self.Root == NodeToDelete:
            return False
        for child in NodeToDelete.Children:
            child.Parent = NodeToDelete.Parent
        NodeToDelete.Parent.Children.extend(NodeToDelete.Children)
        NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        result = [node for node in iter(self)]
        return result

    def FindNodesByValue(self, val):
        result = [node for node in iter(self) if node.NodeValue == val]
        return result

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)

    def Count(self):
        node_counter = 0
        for node in iter(self):
            node_counter += 1
        return node_counter

    def LeafCount(self):
        leaf_counter = 0
        for node in iter(self):
            if len(node.Children) == 0:
                leaf_counter += 1
        return leaf_counter

    def EvenTrees(self):
        """Метод разбивает дерево на максимальное количество минимальных четных деревьев
        на выходе будет список объектов SimpleTreeNode, между которыми нужно разорвать связь"""
        result = []
        def count_DFS(root):
            nonlocal result
            nodes = 1
            for child in root.Children:
                subtree_length = count_DFS(child)
                nodes += subtree_length
            if not root.Children:
                return 1
            if nodes % 2 == 0:
                if root.Parent:
                    result.append(root.Parent)
                    result.append(root)
                return 0
            return nodes
        count_DFS(self.Root)
        return result



class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_lesson_example(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(1, None)
        a_tree.Root = root_node

        two = SimpleTreeNode(2, None)
        a_tree.AddChild(a_tree.Root, two)
        five = SimpleTreeNode(5, None)
        a_tree.AddChild(two, five)
        seven = SimpleTreeNode(7, None)
        a_tree.AddChild(two, seven)

        three = SimpleTreeNode(3, None)
        a_tree.AddChild(a_tree.Root, three)
        four = SimpleTreeNode(4, None)
        a_tree.AddChild(three, four)

        six = SimpleTreeNode(6, None)
        a_tree.AddChild(a_tree.Root, six)
        eight = SimpleTreeNode(8, None)
        a_tree.AddChild(six, eight)
        nine = SimpleTreeNode(9, None)
        a_tree.AddChild(eight, nine)
        ten = SimpleTreeNode(10, None)
        a_tree.AddChild(eight, ten)
        self.assertEqual(a_tree.EvenTrees(), [a_tree.Root, three, a_tree.Root, six])

    def test_another_example(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(1, None)
        a_tree.Root = root_node

        nine = SimpleTreeNode(9, None)
        a_tree.AddChild(a_tree.Root, nine)

        two = SimpleTreeNode(2, None)
        a_tree.AddChild(a_tree.Root, two)
        four = SimpleTreeNode(4, None)
        a_tree.AddChild(two, four)

        three = SimpleTreeNode(3, None)
        a_tree.AddChild(a_tree.Root, three)
        five = SimpleTreeNode(5, None)
        a_tree.AddChild(three, five)
        six = SimpleTreeNode(6, None)
        a_tree.AddChild(five, six)

        self.assertEqual(a_tree.EvenTrees(), [a_tree.Root, two, three, five])

    def tearDown(self):
        pass


unittest.main()