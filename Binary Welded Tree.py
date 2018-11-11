import random

class TreeNode:
    def __init__(self, parent):
        self.parent = parent
        self.left_child = None
        self.left_branch_color = None
        self.right_child = None
        self.right_branch_color = None

class TreeBWT:
    def __init__(self, depth, colors_amount):
        self.root_1 = TreeNode(None)
        self.root_2 = TreeNode(None)
        self.colors_for_branches = []
        for color in range(colors_amount):
            self.colors_for_branches.append(color)
        self.tree_nodes_amount = 0
        for level in range(depth):
            self.tree_nodes_amount += 2**level
        self.build_bwt()

    def build_bwt(self):
        lower_nodes_1 = self.build_tree(self.root_1)
        lower_nodes_2 = self.build_tree(self.root_2)
        self.connect_two_trees(lower_nodes_1, lower_nodes_2)

    def build_tree(self, root):
        root.left_child = TreeNode(root)
        root.left_branch_color = self.colors_for_branches[0]
        root.right_child = TreeNode(root)
        root.right_branch_color = self.colors_for_branches[1]
        nodes_counter = self.tree_nodes_amount - 3
        queue = []
        queue.append(root.left_child)
        queue.append(root.right_child)
        while nodes_counter != 0:
            current_node = queue.pop()
            current_node.left_child = TreeNode(current_node)
            current_node.left_branch_color = self.generate_random_color_for_node(current_node)
            queue.insert(0, current_node.left_child)
            current_node.right_child = TreeNode(current_node)
            current_node.right_branch_color = self.generate_random_color_for_node(current_node)
            queue.insert(0, current_node.right_child)
            nodes_counter -= 2
        return queue

    def connect_two_trees(self, nodes_from_tree_1, nodes_from_tree_2):
        node_queue = nodes_from_tree_2
        for future_parent in nodes_from_tree_1:
            node_for_left_child = node_queue.pop()
            future_parent.left_child = node_for_left_child
            node_for_right_child = node_queue.pop()
            future_parent.right_child = node_for_right_child
            if node_for_left_child.left_child is None:
                node_for_left_child.left_child = future_parent
            else:
                node_for_left_child.right_child = future_parent
            if node_for_right_child.left_child is None:
                node_for_right_child.left_child = future_parent
            else:
                node_for_right_child.right_child = future_parent
            node_queue.insert(0, node_for_left_child)
            node_queue.insert(0, node_for_right_child)

    def generate_random_color_for_node(self, current_node, colors_of_another_tree = None):
        avaliable_colors = set(self.colors_for_branches)
        used_colors = set()
        if colors_of_another_tree:
            used_colors.add(colors_of_another_tree)
        if current_node.left_child:
            used_colors.add(current_node.left_branch_color)
        if current_node.right_child:
            used_colors.add(current_node.right_branch_color)
        if current_node.parent.left_child:
            if current_node.parent.left_child == current_node:
                used_colors.add(current_node.parent.left_branch_color)
        else:
            used_colors.add(current_node.parent.right_branch_color)
        avaliable_colors = list(avaliable_colors.difference(used_colors))
        random_color = avaliable_colors[random.randint(0,len(avaliable_colors)-1)]
        return random_color


new_tree = TreeBWT(3, 4)
