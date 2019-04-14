import unittest
from random import randint, choice

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

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_node(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(15,None)
        a_tree.Root = root_node
        first_child = SimpleTreeNode(25, None)
        a_tree.AddChild(a_tree.Root, first_child)
        self.assertEqual(a_tree.Root.Children[0], first_child)
        self.assertEqual(first_child.Parent, a_tree.Root)

    def test_DeleteNode(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(15, None)
        a_tree.Root = root_node
        tree_nodes = [root_node]
        for i in range(26):
            new_node = SimpleTreeNode(i, None)
            a_tree.AddChild(choice(tree_nodes), new_node)
            tree_nodes.append(new_node)
        self.assertEqual(a_tree.FindNodesByValue(5)[0].NodeValue, 5)
        a_tree.DeleteNode(a_tree.FindNodesByValue(5)[0])
        self.assertEqual(a_tree.FindNodesByValue(5) == [], True)

    def test_count_nodes_and_leafs(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(15, None)
        a_tree.Root = root_node
        first_child = SimpleTreeNode(25, None)
        a_tree.AddChild(a_tree.Root, first_child)
        second_child = SimpleTreeNode(25, None)
        a_tree.AddChild(a_tree.Root, second_child)
        self.assertEqual(a_tree.Count(), 3)
        self.assertEqual(a_tree.LeafCount(), 2)

    def test_iterator_with_break(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(15, None)
        a_tree.Root = root_node
        first_child = SimpleTreeNode(25, None)
        a_tree.AddChild(a_tree.Root, first_child)
        second_child = SimpleTreeNode(25, None)
        a_tree.AddChild(a_tree.Root, second_child)
        counter = 0
        for node in a_tree:
            if counter == 1:
                break
        self.assertEqual(a_tree.Count(), 3)
        self.assertEqual(a_tree.LeafCount(), 2)

    def test_GetAllNodes(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(15, None)
        a_tree.Root = root_node
        tree_nodes = [root_node]
        for i in range(randint(0, 15)):
            new_node = SimpleTreeNode(randint(0, 15), None)
            a_tree.AddChild(choice(tree_nodes), new_node)
            tree_nodes.append(new_node)
        all_nodes = a_tree.GetAllNodes()
        finded_nodes = 0
        for node in all_nodes:
            if node in tree_nodes:
                finded_nodes += 1
        self.assertEqual(finded_nodes, len(tree_nodes))

    def test_MoveNode(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(28, None)
        a_tree.Root = root_node
        last_node = a_tree.Root
        for i in range(26):
            new_node = SimpleTreeNode(i, None)
            a_tree.AddChild(last_node, new_node)
            last_node = new_node
        self.assertEqual(a_tree.FindNodesByValue(15)[0].Parent.NodeValue, 14)
        self.assertEqual(a_tree.FindNodesByValue(15)[0].Children[0].NodeValue, 16)
        a_tree.MoveNode(a_tree.FindNodesByValue(15)[0], a_tree.FindNodesByValue(2)[0])
        self.assertEqual(a_tree.FindNodesByValue(15)[0].Parent.NodeValue, 2)
        self.assertEqual(a_tree.FindNodesByValue(15)[0].Children[0].NodeValue, 16)

    def tearDown(self):
        pass


unittest.main()