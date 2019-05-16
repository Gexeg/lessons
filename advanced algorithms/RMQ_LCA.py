# -*- coding: utf-8 -*-
class Node():
    def __init__(self, start_index, end_index):
        self.start_index = start_index
        self.end_index = end_index
        self.func_value = None
        self.parent = None
        self.childrens = []

class RMA():
    def __init__(self, array, func, up_to_down=True):
        self.array = array
        self.func = func
        self.root = Node(0, len(array)-1)
        if up_to_down:
            self.build_func_tree(0, len(array)-1, self.root)
        else:
            self.build_func_tree_reverse()

    def build_func_tree(self, start_ind, end_ind, root_node):

        if start_ind < end_ind:
            root_node.func_value = self.func(self.array[start_ind:end_ind+1])
            middle = (end_ind-start_ind)//2
            
            first_child = Node(start_ind, start_ind + middle)
            root_node.childrens.append(first_child)
            self.build_func_tree(start_ind, start_ind + middle, first_child)

            second_child = Node(end_ind - middle, end_ind)
            root_node.childrens.append(second_child)
            self.build_func_tree(end_ind - middle, end_ind, second_child)

        if start_ind == end_ind:
            root_node.func_value = self.func([self.array[start_ind]])

    def build_func_tree_reverse(self):
        node_list = []
        for index in range(len(self.array)):
            node = Node(index, index)
            node.func_value = self.func([self.array[index]])
            node_list.append(node)
        self.build_tree_from_leaves(node_list)

    def build_tree_from_leaves(self, node_list):
        if len(node_list) == 1:
            self.root = node_list.pop()
        if len(node_list) > 1:
            parent_node_list = []
            node_counter = len(node_list)
            node_index = 0
            while node_counter > 1:
                first_node = node_list[node_index]
                node_index += 1
                node_counter -= 1
                second_node = node_list[node_index]
                node_index += 1
                node_counter -= 1
                parent_node = Node(first_node.start_index, second_node.end_index)
                parent_node.childrens = [first_node, second_node]
                parent_node.func_value = self.func([first_node.func_value, second_node.func_value])
                parent_node_list.append(parent_node)
            if node_counter == 1:
                parent_node_list.append(node_list[node_index])
            return self.build_tree_from_leaves(parent_node_list)

    def get_func_value(self, start_ind, end_ind, node = None):
        if node == None:
            node = self.root
        if node.start_index == start_ind and node.end_index == end_ind:
            return node.func_value
        for child in node.childrens:
            if child.start_index <= start_ind and child.end_index >= end_ind:
                return self.get_func_value(start_ind, end_ind, child)
        first_value = self.find_start_ind(start_ind, node)
        second_value = self.find_end_ind(end_ind, node)
        return self.func([first_value, second_value])
    
    def find_start_ind(self, start_ind, node):
        for child in node.childrens:
            if child.start_index == start_ind:
                return child.func_value
            elif child.start_index < start_ind:
                return self.find_start_ind(start_ind, child)

    def find_end_ind(self, end_ind, node):
        for child in node.childrens:
            if child.end_index == end_ind:
                return child.func_value
            elif child.end_index > end_ind:
                return self.find_end_ind(end_ind, child)


arr = [i for i in range(10)]
func = lambda x: max(x)
test = RMA(arr, func)

assert test.get_func_value(0,9) == 9, 'неправильное максимальное значение на всем отрезке'
assert test.get_func_value(0,3) == 3, 'неправильное максимальное значение на части отрезка'

arr = [i for i in range(10)]
func = lambda x: max(x)
test = RMA(arr, func, False)

assert test.get_func_value(0,9) == 9, 'неправильное максимальное значение на всем отрезке'
assert test.get_func_value(0,3) == 3, 'неправильное максимальное значение на части отрезка'