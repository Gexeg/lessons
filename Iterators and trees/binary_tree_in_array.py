import unittest

class aBST:
    def __init__(self, depth):
        self.tree_size = (2 ** (depth + 1)) - 1
        self.Tree = [None] * self.tree_size  # массив ключей

    def FindKeyIndex(self, key):
        current_node_index = 0
        while current_node_index < self.tree_size:
            if self.Tree[current_node_index] is None:
                return -current_node_index
            if self.Tree[current_node_index] == key:
                return current_node_index
            elif self.Tree[current_node_index] < key:
                current_node_index = current_node_index * 2 + 2
                if current_node_index not in range(self.tree_size):
                    return None
            elif self.Tree[current_node_index] > key:
                current_node_index = current_node_index * 2 + 1
                if current_node_index not in range(self.tree_size):
                    return None
        return None


    def AddKey(self, key):
        find_result = self.FindKeyIndex(key)
        if find_result == 0:
            self.Tree[0] = key
            return 0
        if find_result is None:
            return -1
        if find_result < 0:
            self.Tree[-find_result] = key
            return -find_result
        if find_result >= 0:
            return -1

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_FindNodeByKey_root(self):
        new_tree = aBST(4)
        self.assertEqual(new_tree.tree_size, 31)
        new_tree = aBST(0)
        self.assertEqual(new_tree.tree_size, 1)
        new_tree = aBST(3)
        self.assertEqual(new_tree.tree_size, 15)

    def test_find_nodes(self):
        new_tree = aBST(2)
        new_tree.Tree = [10, 5, 15, None, None, None, None]
        self.assertEqual(new_tree.FindKeyIndex(5), 1)
        self.assertEqual(new_tree.FindKeyIndex(20), -6)
        keys = [10, 5, 15, 3, 6, 13, 20]
        errors = []
        for key in keys:
            if new_tree.AddKey(key) is False:
                errors.append(key)
        self.assertEqual(new_tree.FindKeyIndex(100), None)

    def test_add_nodes(self):
            new_tree = aBST(2)
            keys = [10, 5, 15, 3, 6, 13, 20]
            errors = []
            for key in keys:
                if new_tree.AddKey(key) is False:
                    errors.append(key)
            print(new_tree.Tree)
            self.assertEqual(len(errors), 0)
            self.assertEqual(None in new_tree.Tree, False)
            self.assertEqual(new_tree.AddKey(16), -1)

    def tearDown(self):
        pass


unittest.main()

