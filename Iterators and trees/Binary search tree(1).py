

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
