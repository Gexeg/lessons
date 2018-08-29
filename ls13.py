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
        self.root = TreeNode(None,root)
        self.current = self.root



    def __iter__(self):
        return self

    def __next__(self):
        node_stack = Stack()
        node_stack.push(self.root)
        if node_stack.size() == 0:
            raise StopIteration
        else:
            node = node_stack.pop()
            for element in node.child:
                node_stack.push(element)
        return node

    def add_tree_node(self, value):
        new_node = TreeNode(self.current, value)
        self.current.child.append(new_node)
        self.current = new_node
        return

    def delete_node(self):
        if self.current == self.root:
            print('Cannot delete root node.')
            return False
        for i in self.current.child:
            i.parent = self.current.parent
        self.current.parent.child.extend(self.current.child)
        self.current = self.current.parent
        return

a_tree = SimpleTree(15)
a_tree.add_tree_node(13)
a_tree.add_tree_node(19)
a_tree.add_tree_node(111)
a_tree.add_tree_node(157)
print(a_tree.current.value)

a_tree.current = a_tree.current.parent
a_tree.add_tree_node(111)
print(a_tree.current.value)

for i in a_tree:
    print(i.value)