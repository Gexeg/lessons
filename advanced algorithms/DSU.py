import random


class Node():
    def __init__(self, value):
        self.parent = None
        self.value = value


class DSU():
    def __init__(self):
        """Система непересекающихся множества. Класс содержит общее множество значений и
        список вершин, помещенных в структуру."""
        self.all_elements = set()
        self.all_nodes = []

    def make_set(self, val):
        """Метод добавляет новый элемент в систему. На вход подается значение. В случае если оно уникально для этой системы,
    создается новое дерево-множество с корнем-представителем """
        if val not in self.all_elements:
            self.all_elements.add(val)
            new_node = Node(val)
            new_node.parent = new_node
            self.all_nodes.append(new_node)

    def find(self, node):
        """Метод ищет представителя дерева-множества, к которому принадлежит данный узел.
        На вход подается узел, на выходе - узел представитель.
        Для сокращения дальнейшего поиска применяется эвристика сжатия пути. Все посещенные узлы собираются в список. Как только
        находится корень-представитель, они связываются напрямую с ним"""
        visited_nodes = []
        current_node = node
        while True:
            if current_node.parent == current_node:
                break
            visited_nodes.append(current_node)
            current_node = current_node.parent
        for node in visited_nodes:
            node.parent = current_node
        return current_node

    def unit(self, node1, node2):
        """Метод люъединяет деревья-множества, содержащие 2 узла. Если эти узлы принадлежат одному множеству,
        то ничего не происходит """
        node_amb1 = self.find(node1)
        node_amb2 = self.find(node2)
        if node_amb1 == node_amb2:
            return
        if random.randint(0, 1) > 0:
            node_amb2.parent = node_amb1
            return
        else:
            node_amb1.parent = node_amb2


test_dsu = DSU()

test_dsu.make_set(11)
test_dsu.make_set(11)
assert len(test_dsu.all_nodes) == 1, 'Добавлен лишний узел'

test_dsu.make_set(15)
assert len(test_dsu.all_nodes) == 2, 'Узел не добавляется'

test_dsu.unit(test_dsu.all_nodes[0], test_dsu.all_nodes[1])
assert test_dsu.find(test_dsu.all_nodes[0]) == test_dsu.find(test_dsu.all_nodes[1]), 'Что-то не так с объединением'

