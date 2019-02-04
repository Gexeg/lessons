class Vertex:
    def __init__(self):
        self.hit = False
        return


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


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

    def find_way_2(self, vertex_1, vertex_2):
        """Поиск пути между вершинами графа через ширину(очередь)"""
        for i in self.vertex:
            i.hit = False
        bfs = Queue()
        parents = {}
        current_vertex = self.vertex[vertex_1]
        current_vertex_index = vertex_1
        bfs.enqueue(current_vertex)
        current_vertex.hit = True
        while True:
            if current_vertex_index == vertex_2:
                path = []
                path.append(current_vertex)
                while True:
                    if parents.get(current_vertex) == None:
                        break
                    path.append(parents.get(current_vertex))
                    current_vertex = parents.get(current_vertex)
                path.reverse()
                return path
            for i in range(self.max_vertex):
                if self.m_adjacency[current_vertex_index][i] == 1 and self.vertex[i].hit is False:
                    parents[self.vertex[i]] = current_vertex
                    bfs.enqueue(self.vertex[i])
                    self.vertex[i].hit = True
            if bfs.size() == 0:
                return None
            current_vertex = bfs.dequeue()
            current_vertex_index = self.vertex.index(current_vertex)


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
new_graph.add_edge(4, 1)


print('Матрица связности')
for i in new_graph.m_adjacency:
    print(i)

print()
print('Поиск пути 0->3')
for i in new_graph.find_way_2(0, 3):
    print(new_graph.vertex.index(i))

print()
print('Поиск пути 4->0')
for i in new_graph.find_way_2(4, 0):
    print(new_graph.vertex.index(i))
