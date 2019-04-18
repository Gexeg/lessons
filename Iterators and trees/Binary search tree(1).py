import unittest


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        current_node = self.Root
        find_result = BSTFind()
        if current_node is None:
            return find_result
        while True:
            if current_node.NodeKey == key:
                find_result.Node = current_node
                find_result.NodeHasKey = True
                return find_result
            elif current_node.NodeKey < key:
                if current_node.RightChild:
                    current_node = current_node.RightChild
                else:
                    find_result.Node = current_node
                    return find_result
            elif current_node.NodeKey > key:
                if current_node.LeftChild:
                    current_node = current_node.LeftChild
                else:
                    find_result.Node = current_node
                    find_result.ToLeft = True
                    return find_result

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        if find_result.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        if find_result.NodeHasKey:
            return False
        if find_result.ToLeft:
            new_node = BSTNode(key, val, find_result.Node)
            find_result.Node.LeftChild = new_node
            return True
        else:
            new_node = BSTNode(key, val, find_result.Node)
            find_result.Node.RightChild = new_node
            return True

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if node is None:
            return None
        if FindMax is False:
            while True:
                if node.LeftChild:
                    node = node.LeftChild
                else:
                    return node
        if FindMax:
            while True:
                if node.RightChild:
                    node = node.RightChild
                else:
                    return node

    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey is False:
            return False

        def parent_child_link(node, key):
            parent_node = node.Parent
            def change_parent_right_child(new_value):
                nonlocal parent_node
                parent_node.RightChild = new_value
            def change_parent_left_child(new_value):
                nonlocal parent_node
                parent_node.LeftChild = new_value
            if node.Parent.RightChild and node.Parent.RightChild.NodeKey == key:
                return change_parent_right_child
            if node.Parent.LeftChild and node.Parent.LeftChild.NodeKey == key:
                return change_parent_left_child

        node = find_result.Node
        if self.Root == node:
            if self.Count() == 1:
                self.Root == None
                return True
            elif node.RightChild is None:
                self.Root.LeftChild.Parent = None
                self.Root = self.Root.LeftChild
                return True
            else:
                new_node = self.FinMinMax(self.Root.RightChild, False)
                while True:
                    if new_node.RightChild is None and new_node.LeftChild is None:
                        new_node_new_parent_link = parent_child_link(new_node, new_node.NodeKey)
                        new_node_new_parent_link(None)
                        new_node.Parent = None
                        if node.LeftChild:
                            new_node.LeftChild = node.LeftChild
                        if node.RightChild:
                            new_node.RightChild = node.RightChild
                        self.Root = new_node
                        return True
                    elif new_node.RightChild:
                        new_node_new_parent_link = parent_child_link(new_node, new_node.NodeKey)
                        new_node_new_parent_link(new_node.RightChild)
                        new_node.RightChild.Parent = new_node.Parent
                        new_node.Parent = None
                        self.Root = new_node
                        if node.LeftChild:
                            new_node.LeftChild = node.LeftChild
                        if node.RightChild:
                            new_node.RightChild = node.RightChild
                        return True

        change_parent_child_link = parent_child_link(node, key)
        if node.RightChild is None and node.LeftChild is None:
            change_parent_child_link(None)
            return True
        elif node.RightChild is None:
            change_parent_child_link(node.LeftChild)
            node.LeftChild.Parent = node.Parent
            return True
        else:
            new_node = self.FinMinMax(node.RightChild, False)
            while True:
                if new_node.RightChild is None and new_node.LeftChild is None:
                    change_parent_child_link(new_node)
                    new_node_new_parent_link = parent_child_link(new_node, new_node.NodeKey)
                    new_node_new_parent_link(None)
                    new_node.Parent = node.Parent
                    if node.LeftChild:
                        new_node.LeftChild = node.LeftChild
                    if node.RightChild:
                        new_node.RightChild = node.RightChild
                    return True
                elif new_node.RightChild:
                    new_node_new_parent_link = parent_child_link(new_node, new_node.NodeKey)
                    new_node_new_parent_link(new_node.RightChild)
                    new_node.RightChild.Parent = new_node.Parent
                    change_parent_child_link(new_node)
                    new_node.Parent = node.Parent
                    if node.LeftChild:
                        new_node.LeftChild = node.LeftChild
                    if node.RightChild:
                        new_node.RightChild = node.RightChild
                    return True

    def Count(self):
        counter = 0
        stack = [self.Root]
        while len(stack) > 0:
            node = stack.pop()
            counter += 1
            if node.RightChild:
                stack.append(node.RightChild)
            if node.LeftChild:
                stack.append(node.LeftChild)
        return counter

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_FindNodeByKey_root(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        self.assertEqual(new_tree.FindNodeByKey(25).Node, new_tree.Root)
        self.assertEqual(new_tree.FindNodeByKey(25).NodeHasKey, True)

    def test_FindNodeByKey_left_child(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        self.assertEqual(new_tree.FindNodeByKey(24).Node, new_tree.Root)
        self.assertEqual(new_tree.FindNodeByKey(24).NodeHasKey, False)
        self.assertEqual(new_tree.FindNodeByKey(24).ToLeft, True)

    def test_FindNodeByKey(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(26, None)
        new_tree.AddKeyValue(55, None)
        new_tree.Root = new_node
        self.assertEqual(new_tree.FindNodeByKey(55).Node, new_tree.Root.RightChild.RightChild)
        self.assertEqual(new_tree.FindNodeByKey(55).NodeHasKey, True)

    def test_AddKeyValue_right_child(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        self.assertEqual(new_tree.FindNodeByKey(26).Node, new_tree.Root)
        self.assertEqual(new_tree.FindNodeByKey(26).NodeHasKey, False)
        self.assertEqual(new_tree.AddKeyValue(26, None), True)
        self.assertEqual(new_tree.Root.RightChild.NodeKey, 26)
        self.assertEqual(new_tree.FindNodeByKey(26).Node, new_tree.Root.RightChild)
        self.assertEqual(new_tree.FindNodeByKey(26).NodeHasKey, True)

    def test_AddKeyValue_left_child(self):
        new_tree = BST(None)
        new_node = BSTNode(25, 30, None)
        new_tree.Root = new_node
        self.assertEqual(new_tree.FindNodeByKey(14).Node, new_tree.Root)
        self.assertEqual(new_tree.FindNodeByKey(14).NodeHasKey, False)
        self.assertEqual(new_tree.AddKeyValue(14, 45), True)
        self.assertEqual(new_tree.Root.LeftChild.NodeKey, 14)
        self.assertEqual(new_tree.FindNodeByKey(14).Node, new_tree.Root.LeftChild)
        self.assertEqual(new_tree.FindNodeByKey(14).NodeHasKey, True)

    def test_AddKeyValue_empty_tree(self):
        new_tree = BST(None)
        self.assertEqual(new_tree.AddKeyValue(14, 45), True)
        self.assertEqual(new_tree.FindNodeByKey(14).Node, new_tree.Root)

    def test_AddKeyValue_tree_has_key(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(25, 15)
        self.assertEqual(new_tree.AddKeyValue(25, 15), False)
        self.assertEqual(new_tree.Root.RightChild, None)
        self.assertEqual(new_tree.Root.LeftChild, None)

    def test_AddKeyValue_more_nodes_in_tree_right(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(25, 1)
        new_tree.AddKeyValue(65, 3)
        new_tree.AddKeyValue(57, 15)
        new_tree.AddKeyValue(78, None)
        self.assertEqual(new_tree.FindNodeByKey(0).NodeHasKey, False)
        new_tree.AddKeyValue(0, None)
        self.assertEqual(new_tree.FindNodeByKey(0).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(0).Node.Parent, new_tree.FindNodeByKey(25).Node)

    def test_AddKeyValue_more_nodes_in_tree_left(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(25, 1)
        new_tree.AddKeyValue(65, 3)
        new_tree.AddKeyValue(57, 15)
        new_tree.AddKeyValue(78, None)
        self.assertEqual(new_tree.FindNodeByKey(8).NodeHasKey, False)
        new_tree.AddKeyValue(8, None)
        self.assertEqual(new_tree.FindNodeByKey(8).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(8).Node.Parent, new_tree.FindNodeByKey(25).Node)

    def test_FindMinMax_only_root(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        self.assertEqual(new_tree.FinMinMax(new_tree.Root, True), new_tree.Root)
        self.assertEqual(new_tree.FinMinMax(new_tree.Root, False), new_tree.Root)

    def test_FindMinMax_root(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(14, None)
        self.assertEqual(new_tree.FinMinMax(new_tree.Root, True), new_tree.Root.RightChild)
        self.assertEqual(new_tree.FinMinMax(new_tree.Root, True).NodeKey, 36)
        self.assertEqual(new_tree.FinMinMax(new_tree.Root, False), new_tree.Root.LeftChild)
        self.assertEqual(new_tree.FinMinMax(new_tree.Root, False).NodeKey, 14)

    def test_FindMinMax_tree(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(44, None)
        new_tree.AddKeyValue(27, None)
        new_tree.AddKeyValue(14, None)
        new_tree.AddKeyValue(18, None)
        self.assertEqual(new_tree.FinMinMax(new_tree.FindNodeByKey(36).Node, True), new_tree.Root.RightChild.RightChild)
        self.assertEqual(new_tree.FinMinMax(new_tree.FindNodeByKey(36).Node, True).NodeKey, 44)
        self.assertEqual(new_tree.FinMinMax(new_tree.FindNodeByKey(36).Node, False), new_tree.Root.RightChild.LeftChild)
        self.assertEqual(new_tree.FinMinMax(new_tree.FindNodeByKey(36).Node, False).NodeKey, 27)
        self.assertEqual(new_tree.FinMinMax(new_tree.FindNodeByKey(14).Node, True), new_tree.Root.LeftChild.RightChild)
        self.assertEqual(new_tree.FinMinMax(new_tree.FindNodeByKey(14).Node, True).NodeKey, 18)

    def test_del_node_without_childrens(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        self.assertEqual(new_tree.FindNodeByKey(36).NodeHasKey, True)
        new_tree.DeleteNodeByKey(36)
        self.assertEqual(new_tree.FindNodeByKey(36).NodeHasKey, False)
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(14, None)
        new_tree.AddKeyValue(27, None)
        self.assertEqual(new_tree.DeleteNodeByKey(25), True)
        self.assertEqual(new_tree.Root.NodeKey, 27)
        self.assertEqual(new_tree.FindNodeByKey(25).NodeHasKey, False)
        self.assertEqual(new_tree.Count(), 3)

    def test_del_root_node_with_childrens(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(14, None)
        new_tree.AddKeyValue(27, None)
        new_tree.AddKeyValue(29, None)
        new_tree.AddKeyValue(29, None)
        self.assertEqual(new_tree.DeleteNodeByKey(25), True)
        self.assertEqual(new_tree.Root.NodeKey, 27)
        self.assertEqual(new_tree.FindNodeByKey(25).NodeHasKey, False)
        self.assertEqual(new_tree.Count(), 4)


    def test_del_node_with_left_child(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(28, None)
        new_tree.AddKeyValue(29, None)
        self.assertEqual(new_tree.FindNodeByKey(36).NodeHasKey, True)
        new_tree.DeleteNodeByKey(36)
        self.assertEqual(new_tree.FindNodeByKey(36).NodeHasKey, False)
        self.assertEqual(new_tree.FindNodeByKey(28).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(28).Node, new_tree.Root.RightChild)
        self.assertEqual(new_tree.FindNodeByKey(29).Node, new_tree.FindNodeByKey(28).Node.RightChild)

    def test_del_node_with_left_right_child(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(38, None)
        new_tree.AddKeyValue(28, None)
        new_tree.AddKeyValue(29, None)
        self.assertEqual(new_tree.FindNodeByKey(36).NodeHasKey, True)
        self.assertEqual(new_tree.Count(), 5)
        new_tree.DeleteNodeByKey(36)
        self.assertEqual(new_tree.FindNodeByKey(36).NodeHasKey, False)
        self.assertEqual(new_tree.Count(), 4)
        self.assertEqual(new_tree.FindNodeByKey(38).Node, new_tree.Root.RightChild)
        self.assertEqual(new_tree.FindNodeByKey(29).Node.NodeValue, new_tree.FindNodeByKey(28).Node.RightChild.NodeValue)


    def test_del_node_empty_tree(self):
        new_tree = BST(None)
        self.assertEqual(new_tree.DeleteNodeByKey(25), False)

    def test_Count_nodes(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(14, None)
        self.assertEqual(new_tree.Count(), 3)

    def test_Count_nodes_after_remove(self):
        new_tree = BST(None)
        new_node = BSTNode(25, None, None)
        new_tree.Root = new_node
        new_tree.AddKeyValue(36, None)
        new_tree.AddKeyValue(92, None)
        new_tree.AddKeyValue(76, None)
        new_tree.AddKeyValue(85, None)
        new_tree.AddKeyValue(34, None)
        new_tree.AddKeyValue(79, None)
        new_tree.AddKeyValue(14, None)
        self.assertEqual(new_tree.Count(), 8)
        new_tree.DeleteNodeByKey(36)
        self.assertEqual(new_tree.Count(), 7)
        self.assertEqual(new_tree.FindNodeByKey(25).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(36).NodeHasKey, False)
        self.assertEqual(new_tree.FindNodeByKey(92).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(76).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(85).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(34).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(79).NodeHasKey, True)
        self.assertEqual(new_tree.FindNodeByKey(14).NodeHasKey, True)

    def tearDown(self):
        pass


unittest.main()