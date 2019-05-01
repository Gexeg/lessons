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