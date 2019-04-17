
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
            return
        if find_result.NodeHasKey:
            return False
        if find_result.ToLeft:
            new_node = BSTNode(key, val, find_result.Node)
            find_result.Node.LeftChild = new_node
        else:
            new_node = BSTNode(key, val, find_result.Node)
            find_result.Node.RightChild = new_node

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
        node = find_result.Node
        if self.Root == node:
            return False
        if node.RightChild is None and node.LeftChild is None:
            if node.Parent.RightChild and node.Parent.RightChild.NodeKey == key:
                node.Parent.RightChild = None
                return
            if node.Parent.LeftChild and node.Parent.LeftChild.NodeKey == key:
                node.Parent.LeftChild = None
                return
        elif node.RightChild is None:
            if node.Parent.RightChild and node.Parent.RightChild.NodeKey == key:
                node.Parent.RightChild = node.LeftChild
                node.LeftChild.Parent = node.Parent
                return
            if node.Parent.LeftChild and node.Parent.LeftChild.NodeKey == key:
                node.Parent.LeftChild = node.LeftChild
                node.LeftChild.Parent = node.Parent
                return
        else:
            new_node = node.RightChild
            while True:
                if new_node.RightChild is None and new_node.LeftChild is None:
                    if node.Parent.RightChild and node.Parent.RightChild.NodeKey == key:
                        node.Parent.RightChild = new_node
                        new_node.Parent = node.Parent
                        return
                    if node.Parent.LeftChild and node.Parent.LeftChild.NodeKey == key:
                        node.Parent.LeftChild = None
                        new_node.Parent = node.Parent
                        return
                if new_node.LeftChild:
                    new_node = new_node.LeftChild
                else:
                    if node.Parent.RightChild and node.Parent.RightChild.NodeKey == key:
                        node.Parent.RightChild = new_node
                        new_node.Parent = node.Parent
                        return
                    if node.Parent.LeftChild and node.Parent.LeftChild.NodeKey == key:
                        node.Parent.LeftChild = None
                        new_node.Parent = node.Parent
                        return

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
