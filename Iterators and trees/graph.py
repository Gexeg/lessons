import unittest

class Vertex:

    def __init__(self, val):
        self.Value = val


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


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_first_vertex(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(15)
        self.assertEqual(new_graph.vertex[0].Value, 15)

    def test_add_vertex(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(15)
        new_graph.AddVertex(18)
        new_graph.AddVertex(224)
        new_graph.AddVertex(235)
        new_graph.AddVertex(257)
        new_graph.AddVertex(678)
        new_graph.AddVertex(19)
        self.assertEqual(len(new_graph.vertex), 5)
        self.assertEqual(new_graph.vertex[4].Value, 257)
        for row in new_graph.m_adjacency:
            for edge in row:
                self.assertEqual(edge, 0)

    def test_add_edge(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(15)
        new_graph.AddVertex(18)
        new_graph.AddVertex(224)
        new_graph.AddVertex(235)
        new_graph.AddVertex(257)
        new_graph.AddVertex(678)
        new_graph.AddEdge(0, 4)
        self.assertEqual(new_graph.m_adjacency[0][4], 1)
        self.assertEqual(new_graph.m_adjacency[4][0], 1)
        new_graph.AddEdge(3, 2)
        self.assertEqual(new_graph.m_adjacency[2][3], 1)
        self.assertEqual(new_graph.m_adjacency[3][2], 1)
        new_graph.AddEdge(0, 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)

    def test_remove_edge(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(1)
        new_graph.AddVertex(15)
        new_graph.AddVertex(12)
        new_graph.AddEdge(0, 1)
        self.assertEqual(new_graph.m_adjacency[0][1], 1)
        self.assertEqual(new_graph.m_adjacency[1][0], 1)
        new_graph.RemoveEdge(0, 1)
        self.assertEqual(new_graph.m_adjacency[0][1], 0)
        self.assertEqual(new_graph.m_adjacency[1][0], 0)
        new_graph.AddEdge(0, 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)
        new_graph.RemoveEdge(0, 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 0)

    def test_remove_vertex(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(1)
        new_graph.AddVertex(15)
        new_graph.AddVertex(12)
        new_graph.AddEdge(0, 1)
        new_graph.AddEdge(0, 2)
        self.assertEqual(new_graph.m_adjacency[0][1], 1)
        self.assertEqual(new_graph.m_adjacency[1][0], 1)
        self.assertEqual(new_graph.m_adjacency[0][2], 1)
        self.assertEqual(new_graph.m_adjacency[2][0], 1)
        new_graph.RemoveVertex(0)
        self.assertEqual(new_graph.m_adjacency[0][1], 0)
        self.assertEqual(new_graph.m_adjacency[1][0], 0)
        self.assertEqual(new_graph.m_adjacency[0][2], 0)
        self.assertEqual(new_graph.m_adjacency[2][0], 0)

    def tearDown(self):
        pass

unittest.main()