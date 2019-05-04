class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = []

    def AddVertex(self, v):
        """Добавление вершины графа"""
        if len(self.vertex) >= self.max_vertex:
            return
        new_vertex = Vertex(v)
        self.vertex.append(new_vertex)

    def RemoveVertex(self, vertex_ind):
        """Удаление вершины и всех ребер, связывающих её с другими по индексу вершины"""
        if vertex_ind > len(self.vertex) - 1:
            return
        chained_with = []
        adj_vertex_ind = 0
        for edge in self.m_adjacency[vertex_ind]:
            if edge == 1:
                chained_with.append(adj_vertex_ind)
            adj_vertex_ind += 1
        for adj_vertex_i in chained_with:
            self.RemoveEdge(vertex_ind, adj_vertex_i)

    def IsEdge(self, v1, v2):
        """Есть ли между вершинами связь? (необходимо ввести индексы вершин)"""
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return False
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        """Добавление ребра между двумя вершинами графа (необходимо ввести индексы вершин)"""
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        """Удаление ребра между двумя вершинами графа (необходимо ввести индексы вершин)"""
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return False
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, from_vertex, to_vertex):
        """Поиск пути от одного узла к другому через обход в глубину"""
        if from_vertex > len(self.vertex) or to_vertex > len(self.vertex):
            return []
        for vertex in self.vertex:
            vertex.Hit = False
        way = []
        current_vertex = self.vertex[from_vertex]
        current_vertex_index = from_vertex
        way.append(current_vertex)
        current_vertex.Hit = True
        while way:
            if self.vertex[from_vertex] in way and self.vertex[to_vertex] in way:
                return way
            for vertex in range(self.max_vertex):
                if self.m_adjacency[current_vertex_index][vertex] == 1 and self.vertex[vertex].Hit is False:
                    current_vertex = self.vertex[vertex]
                    current_vertex_index = vertex
                    current_vertex.Hit = True
                    way.append(current_vertex)
                    break
                """Если путь зашел не туда"""
                if vertex == self.max_vertex - 1:
                    way.pop()
                    if way:
                        current_vertex_index = self.vertex.index(way[-1])
        return []
