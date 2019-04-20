
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
