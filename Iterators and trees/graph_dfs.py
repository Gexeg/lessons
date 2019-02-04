class Vertex:
    def __init__(self):
        self.hit = False
        return


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(-1)

    def push(self, value):
        return self.stack.append(value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class SimpleGraph:
    def __init__(self, max_vert):
        self.max_vertex = max_vert
        self.vertex = []
        self.m_adjacency = []
        for i in range(self.max_vertex):
            new_vertex = []
            self.m_adjacency.append(new_vertex)
            for j in range(self.max_vertex):
                new_vertex.append(0)

    def add_vertex(self):
        """Добавление вершины графа"""
        if len(self.vertex) >= self.max_vertex:
            return None
        new_vertex = Vertex()
        self.vertex.append(new_vertex)
        return

    def add_edge(self, vertex_1, vertex_2):
        """Добавление ребра между двумя вершинами графа.
        Ребро однонаправлено от 1 вершины ко 2. (необходимо ввести индексы вершин)"""
        if vertex_1 > len(self.vertex)-1 or vertex_2 > len(self.vertex)-1 or vertex_1 == vertex_2:
            return False
        self.m_adjacency[vertex_1][vertex_2] = 1
        return

    def del_edge(self, vertex_1, vertex_2):
        """Удаление ребра между двумя вершинами графа (необходимо ввести индексы вершин)"""
        if vertex_1 > len(self.vertex) - 1 or vertex_2 > len(self.vertex) - 1 or vertex_1 == vertex_2:
            return False
        self.m_adjacency[vertex_1][vertex_2] = 0
        self.m_adjacency[vertex_2][vertex_1] = 0
        return

    def del_vertex(self, vertex):
        """Удаление вершины и всех ребер, связывающих её с другими по индексу вершины"""
        if vertex > len(self.vertex) - 1:
            return False
        for i in range(self.max_vertex):
            self.m_adjacency[vertex][i]=0
        for elem in self.m_adjacency:
            elem[0] = 0
        return

    def find_way(self, vertex_1, vertex_2):
        """Поиск пути между вершинами графа через глубину(стек)"""
        for i in self.vertex:
            i.hit = False
        way = Stack()
        current_vertex = self.vertex[vertex_1]
        current_vertex_index = vertex_1
        way.push(current_vertex)
        current_vertex.hit = True
        while True:
            if self.vertex[vertex_1] in way.stack and self.vertex[vertex_2] in way.stack:
                return way.stack
            for i in range(self.max_vertex):
                if self.m_adjacency[current_vertex_index][i] == 1 and self.vertex[i].hit is False:
                    current_vertex = self.vertex[i]
                    current_vertex_index = i
                    current_vertex.hit = True
                    way.push(current_vertex)
                    break
                if i == self.max_vertex - 1:
                    way.pop()
                    if way.size() == 0:
                        return None
                    current_vertex_index = self.vertex.index(way.peak())
        return None


new_graph = SimpleGraph(5)
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()

new_graph.add_edge(0, 2)
new_graph.add_edge(1, 0)
new_graph.add_edge(0, 3)
new_graph.add_edge(4, 2)
new_graph.add_edge(2, 3)
new_graph.add_edge(2, 1)

print('Матрица связности')
for i in new_graph.m_adjacency:
    print(i)

print()
print('Поиск пути 0->3')
for i in new_graph.find_way(0, 3):
    print(new_graph.vertex.index(i))

print()
print('Поиск пути 4->0')
for i in new_graph.find_way(4, 0):
    print(new_graph.vertex.index(i))
