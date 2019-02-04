class Vertex:
    def __init__(self):
        return

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
        """Добавление ребра между двумя вершинами графа (необходимо ввести индексы вершин)"""
        if vertex_1 > len(self.vertex)-1 or vertex_2 > len(self.vertex)-1 or vertex_1 == vertex_2:
            return False
        self.m_adjacency[vertex_1][vertex_2] = 1
        self.m_adjacency[vertex_2][vertex_1] = 1
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
        chained_with = []
        t = 0
        for i in self.m_adjacency[vertex]:
            if i == 1:
                chained_with.append(t)
                self.m_adjacency[vertex][t] = 0
            t +=1
        for elem in chained_with:
            self.m_adjacency[elem][vertex] = 0
        return

new_graph = SimpleGraph(5)
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()
new_graph.add_vertex()

new_graph.add_edge(0, 2)
new_graph.add_edge(0, 1)
new_graph.add_edge(0,3)
new_graph.add_edge(4,2)

print('Матрица до удаления узла')
for i in new_graph.m_adjacency:
    print(i)

new_graph.del_vertex(0)
print()
print('Узел и все его связи удалены')
for i in new_graph.m_adjacency:
    print(i)
