import random, timeit

class WanderingNode:
    def __init__(self, parent_node):
        self.location = parent_node

    def step(self):
        if self.location.parent:
            possible_directions = set(['parent','left_child','right_child'])
            direction = random.sample(possible_directions, 1)[0]
        else:
            possible_directions = set(['left_child', 'right_child'])
            direction = random.sample(possible_directions, 1)[0]
        if direction == 'parent':
            self.location = self.location.parent
        elif direction == 'left_child':
            self.location = self.location.left_child
        elif direction == 'right_child':
            self.location = self.location.right_child

class TreeNode:
    def __init__(self, parent, index):
        self.parent = parent
        self.index = index
        self.left_child = None
        self.right_child = None


class TreeBWT:
    def __init__(self, depth):
        self.roots = []
        self.matrix_of_adajency = {}
        self.max_node_index = 0
        self.colors_for_branches = set(['red','blue','green','yellow'])
        self.single_tree_depth = depth
        self.node_amount = 2 ** depth - 1

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
        node_counter = 0
        while node_counter < self.node_amount:
            next_level = []
            for node in current_level:
                print(node.index, self.matrix_of_adajency[node.index], end=' --  ')
                next_level.append(node.left_child)
                next_level.append(node.right_child)
                node_counter += 1
            print()
            current_level = next_level

    def print_reverse_tree(self):
        current_level = [self.roots[1]]
        node_counter = 0
        tree_depth = 0
        all_revers_tree_nodes = []
        while node_counter < self.node_amount:
            next_level = []
            for node in current_level:
                all_revers_tree_nodes.append(node)
                next_level.append(node.left_child)
                next_level.append(node.right_child)
                node_counter += 1
            current_level = next_level
            tree_depth += 1
        while tree_depth > 0:
            tree_depth -= 1
            nodes_by_level = 2**tree_depth
            for node in range(nodes_by_level):
                node_counter = all_revers_tree_nodes.pop()
                print(node_counter.index, self.matrix_of_adajency[node_counter.index], end=' --  ')
            print()

    def find_way_vertex_to_vertex(self, color):
        first_way = self.find_way_vertex_to_foot(self.roots[0])
        second_way = self.find_way_vertex_to_foot(self.roots[1])
        all_ways = self.combine_ways(first_way, second_way)
        colored_ways = self.add_colors(all_ways)
        desired_way = self.choose_best_way(colored_ways, color)
        return colored_ways, desired_way

    def find_way_vertex_to_foot(self, root):
        parents = {}
        node_counter = 0
        current_node_index = root.index
        for node in range(self.node_amount):
            for child in self.matrix_of_adajency[current_node_index]:
                parents[child] = current_node_index
            node_counter += 1
            current_node_index += 1
        foot_nodes_indexes = []
        last_index = root.index + self.node_amount - 1
        for node_index in range(2**(self.single_tree_depth-1)):
            foot_nodes_indexes.append(last_index)
            last_index -= 1
        ways = []
        for node in foot_nodes_indexes:
            path = []
            path.append(node)
            while True:
                if parents.get(node) is None:
                    path.reverse()
                    ways.append(path)
                    break
                path.append(parents.get(node))
                node = parents.get(node)
        return ways

    def combine_ways(self, first_ways, second_ways):
        combined_ways = []
        for path in first_ways:
            first_foot_node_index = path[-1]
            first_foot_node_child_indexes = list(self.matrix_of_adajency[first_foot_node_index].keys())
            for path_2 in second_ways:
                second_foot_node_index = path_2[-1]
                if second_foot_node_index in first_foot_node_child_indexes:
                    first_path = list(path)
                    second_path = list(path_2)
                    second_path.reverse()
                    first_path.extend(second_path)
                    combined_ways.append(first_path)
        return combined_ways

    def add_colors(self, ways):
        ways_with_color = []
        for path in ways:
            branches_color = []
            for node_index in range(self.single_tree_depth):
                branches_color.append(self.matrix_of_adajency[path[node_index]][path[node_index + 1]])
            second_tree_nodes = list(path[self.single_tree_depth:])
            second_tree_nodes.reverse()
            second_tree_branches_color = []
            for node_index in range(self.single_tree_depth-1):
                second_tree_branches_color.append(self.matrix_of_adajency[second_tree_nodes[node_index]][second_tree_nodes[node_index + 1]])
            second_tree_branches_color.reverse()
            branches_color.extend(second_tree_branches_color)
            ways_with_color.append((path,branches_color))
        return ways_with_color

    def choose_best_way(self, ways, desired_color):
        count_desired_colors = []
        for path_and_colors in ways:
            color_counter = 0
            for color in path_and_colors[1]:
                if color == desired_color:
                    color_counter +=1
            count_desired_colors.append(color_counter)
        return ways[count_desired_colors.index(min(count_desired_colors))]

    def find_node_by_random_movements(self, desired_index):
        if desired_index > self.node_amount*2:
            return False
        searching_node = WanderingNode(self.roots[0])
        while True:
            searching_node.step()
            if searching_node.location.index == desired_index:
                return searching_node.location, searching_node.location.index

    def find_node_by_quantum_random_movements(self, desired_index):
        if desired_index > self.node_amount*2:
            return False
        searching_swarm = [WanderingNode(self.roots[0])]
        while len(searching_swarm) < 100000:
            for node in searching_swarm:
                new_searching_node = WanderingNode(node.location)
                searching_swarm.append(new_searching_node)
                node.step()
                if node.location.index == desired_index:
                    return node.location, node.location.index, len(searching_swarm)
                new_searching_node.step()
                if new_searching_node.location.index == desired_index:
                    return new_searching_node.location, new_searching_node.location.index, len(searching_swarm)


new_tree = TreeBWT(10)
new_tree.build_color_reverse_bwt()
new_tree.print_bwt()
print()
find_way = new_tree.find_way_vertex_to_vertex('green')
print(find_way[1])

time_for_find_element = timeit.Timer(lambda: new_tree.find_node_by_random_movements(random.randint(1, new_tree.node_amount*2))).timeit(number=100)
time_for_find_element2 = timeit.Timer(lambda: new_tree.find_node_by_quantum_random_movements(random.randint(1, new_tree.node_amount*2))).timeit(number=100)

time_list = []
time_list.append(time_for_find_element / 100)
time_list.append(time_for_find_element2 / 100)

print('Время нахождения узла с помощью алгоритма блуждания: ', time_list[0])
print('Время нахождения узла с помощью квантовой реализации алгоритма блуждания: ', time_list[1])