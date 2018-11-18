import random


class TreeNode:
    def __init__(self, parent, index):
        self.parent = parent
        self.index = index
        self.left_child = None
        self.right_child = None


class TreeBWT:
    def __init__(self, depth, colors_amount):
        self.roots = []
        self.matrix_of_adajency = {}
        self.max_node_index = 0
        self.colors_for_branches = set()
        for color in range(colors_amount):
            self.colors_for_branches.add(color)
        self.node_amount = 0
        for level in range(depth):
            self.node_amount += 2 ** level

    def build_bwt(self):
        first_tree_nodes = self.build_tree()
        second_tree_nodes = self.build_tree()
        self.connect_two_trees(first_tree_nodes, second_tree_nodes)

    def build_tree(self):
        queue = [self.create_root_node()]
        node_amount = self.node_amount - 1
        while node_amount != 0:
            current_node = queue.pop()
            self.create_left_child_node(current_node)
            queue.insert(0, current_node.left_child)
            self.create_right_child_node(current_node)
            queue.insert(0, current_node.right_child)
            node_amount -= 2
        return queue

    def build_color_reverse_bwt(self):
        first_tree_nodes = self.build_tree()
        second_tree_nodes = self.build_color_reverse_tree()
        self.connect_two_trees(first_tree_nodes, second_tree_nodes)

    def build_color_reverse_tree(self):
        queue = [self.create_root_node()]
        mirror_node_index = 1
        node_amount = self.node_amount - 1
        while node_amount != 0:
            current_node = queue.pop()
            avaliable_colors = list(self.matrix_of_adajency[mirror_node_index].values())
            current_node.left_child = TreeNode(current_node, self.max_node_index + 1)
            self.max_node_index += 1
            self.matrix_of_adajency[current_node.index][current_node.left_child.index] = avaliable_colors[1]
            self.matrix_of_adajency[current_node.left_child.index] = {}
            queue.insert(0, current_node.left_child)
            current_node.right_child = TreeNode(current_node, self.max_node_index + 1)
            self.max_node_index += 1
            self.matrix_of_adajency[current_node.index][current_node.right_child.index] = avaliable_colors[0]
            self.matrix_of_adajency[current_node.right_child.index] = {}
            queue.insert(0, current_node.right_child)
            mirror_node_index += 1
            node_amount -= 2
        return queue

    def connect_two_trees(self, first_nodes, second_nodes):
        for index in range(len(first_nodes)):
            first_nodes[index].left_child = second_nodes[index]
            second_nodes[index].left_child = first_nodes[index]
            branch_color = self.generate_random_color(first_nodes[index], second_nodes[index])
            self.matrix_of_adajency[first_nodes[index].index][second_nodes[index].index] = branch_color
            self.matrix_of_adajency[second_nodes[index].index][first_nodes[index].index] = branch_color
            first_nodes[index].right_child = second_nodes[index - 1]
            second_nodes[index - 1].right_child = first_nodes[index]
            branch_color = self.generate_random_color(first_nodes[index], second_nodes[index - 1])
            self.matrix_of_adajency[first_nodes[index].index][second_nodes[index - 1].index] = branch_color
            self.matrix_of_adajency[second_nodes[index - 1].index][first_nodes[index].index] = branch_color

    def create_root_node(self):
        root = TreeNode(None, self.max_node_index + 1)
        self.roots.append(root)
        self.max_node_index += 1
        self.matrix_of_adajency[root.index] = {}
        return root

    def create_left_child_node(self, parent_node):
        parent_node.left_child = TreeNode(parent_node, self.max_node_index + 1)
        self.max_node_index += 1
        self.matrix_of_adajency[parent_node.left_child.index] = {}
        self.matrix_of_adajency[parent_node.index][parent_node.left_child.index] = self.generate_random_color(
            parent_node)

    def create_right_child_node(self, parent_node):
        parent_node.right_child = TreeNode(parent_node, self.max_node_index + 1)
        self.max_node_index += 1
        self.matrix_of_adajency[parent_node.right_child.index] = {}
        self.matrix_of_adajency[parent_node.index][parent_node.right_child.index] = self.generate_random_color(
            parent_node)

    def generate_random_color(self, node, another_node=None):
        used_colors = set()
        if another_node:
            used_colors.add(self.matrix_of_adajency[another_node.parent.index][another_node.index])
        if node.parent:
            used_colors.add(self.matrix_of_adajency[node.parent.index][node.index])
        for color in self.matrix_of_adajency[node.index].values():
            used_colors.add(color)
        available_colors = list(self.colors_for_branches.difference(used_colors))
        random_color = available_colors[random.randint(0, len(available_colors) - 1)]
        return random_color

    def print_bwt(self):
        self.print_firtst_tree()
        print()
        self.print_reverse_tree()

    def print_firtst_tree(self):
        current_level = [self.roots[0]]
        current_node_index = 0
        while current_node_index < self.node_amount:
            next_level = []
            for node in current_level:
                print(node.index, self.matrix_of_adajency[node.index], end=' --  ')
                next_level.append(node.left_child)
                next_level.append(node.right_child)
                current_node_index += 1
            print()
            current_level = next_level

    def print_reverse_tree(self):
        current_level = [self.roots[1]]
        current_node_index = 0
        tree_depth = 0
        all_revers_tree_nodes = []
        while current_node_index < self.node_amount:
            next_level = []
            for node in current_level:
                all_revers_tree_nodes.append(node)
                next_level.append(node.left_child)
                next_level.append(node.right_child)
                current_node_index += 1
            current_level = next_level
            tree_depth += 1
        while tree_depth > 0:
            tree_depth -= 1
            nodes_by_level = 2**tree_depth
            for node in range(nodes_by_level):
                current_node = all_revers_tree_nodes.pop()
                print(current_node.index, self.matrix_of_adajency[current_node.index], end=' --  ')
            print()


new_tree = TreeBWT(3, 4)
new_tree.build_bwt()
new_tree.print_bwt()
