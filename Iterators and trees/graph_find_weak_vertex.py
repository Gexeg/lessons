import unittest
from random import randint


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


    def BreadthFirstSearch(self, from_vertex, to_vertex):
        '''Поиск пути от одного узла к другому через обход в глубину'''
        if from_vertex > len(self.vertex) or to_vertex > len(self.vertex):
            return []
        for vertex in self.vertex:
            vertex.Hit = False
        queue = []
        '''Т.к. в узле нет информации о родителе, то её необходимо собирать во время построения пути'''
        parent_map = {}
        current_vertex = self.vertex[from_vertex]
        cur_vertex_ind = from_vertex
        queue.insert(0, current_vertex)
        current_vertex.Hit = True
        while True:
            if cur_vertex_ind == to_vertex:
                '''Если узел найден, восстанавливаем путь от последнего узла с помощью карты родителей 
                и переворачиваем его.'''
                path = []
                path.append(current_vertex)
                while True:
                    if parent_map.get(current_vertex) is None:
                        break
                    path.append(parent_map.get(current_vertex))
                    current_vertex = parent_map.get(current_vertex)
                path.reverse()
                return path
            for vertex_ind in range(self.max_vertex):
                if self.m_adjacency[cur_vertex_ind][vertex_ind] == 1 and self.vertex[vertex_ind].Hit is False:
                    '''Поскольку мы не знаем какая дорога приведет к искомому узлу, необходимо сохранять всех 
                    родителей в карту'''
                    parent_map[self.vertex[vertex_ind]] = current_vertex
                    queue.insert(0, self.vertex[vertex_ind])
                    self.vertex[vertex_ind].Hit = True
            if queue:
                current_vertex = queue.pop()
                cur_vertex_ind = self.vertex.index(current_vertex)
            else:
                return []

    def WeakVertices(self):
        """Метод находит вершины, которые не входят в треугольную структуру.
        Используется ндругая матрица смежности"""
        adajecency_map ={}
        for first_vertex_ind in range(len(self.vertex)):
            adajecency_map[str(first_vertex_ind)] = []
            for vertex_ind in range(self.max_vertex):
                if self.m_adjacency[first_vertex_ind][vertex_ind] == 1:
                    adajecency_map[str(first_vertex_ind)].append(vertex_ind)
        """Если у текущей вершины есть 2 смежных, которые смежны между собой, то вместе 
        они образуют треугольник"""
        weak_vertex = []
        for key in adajecency_map.keys():
            strong_edges = 0
            for adj_vertex in adajecency_map[key]:
                adj_vertex_roster = set(adajecency_map[str(adj_vertex)])
                if len(adj_vertex_roster.intersection(adajecency_map[key])) > 0:
                    strong_edges += 1
                    break
            if strong_edges == 0:
                weak_vertex.append(self.vertex[int(key)])
        return weak_vertex


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_weak_nodex_complex_structure(self):
        new_graph = SimpleGraph(10)

        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))

        new_graph.AddEdge(0, 1)
        new_graph.AddEdge(0, 2)
        new_graph.AddEdge(1, 2)
        new_graph.AddEdge(1, 4)
        new_graph.AddEdge(2, 3)
        new_graph.AddEdge(2, 4)
        new_graph.AddEdge(2, 5)
        new_graph.AddEdge(4, 6)
        new_graph.AddEdge(5, 6)
        new_graph.AddEdge(5, 7)
        new_graph.AddEdge(6, 7)
        new_graph.AddEdge(6, 8)
        new_graph.AddEdge(8, 9)

        weak_vertex_indexes = []
        for vertex in new_graph.WeakVertices():
            weak_vertex_indexes.append(new_graph.vertex.index(vertex))
        self.assertEqual(weak_vertex_indexes, [3, 8, 9])

    def test_find_weak_nodex_empty_graph(self):
        new_graph = SimpleGraph(10)

        weak_vertex_indexes = []
        for vertex in new_graph.WeakVertices():
            weak_vertex_indexes.append(new_graph.vertex.index(vertex))
        self.assertEqual(weak_vertex_indexes, [])

    def test_find_weak_nodex_two_triangle(self):
        new_graph = SimpleGraph(4)

        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))

        new_graph.AddEdge(0, 1)
        new_graph.AddEdge(0, 2)
        new_graph.AddEdge(1, 2)
        new_graph.AddEdge(1, 3)
        new_graph.AddEdge(2, 3)

        weak_vertex_indexes = []
        for vertex in new_graph.WeakVertices():
            weak_vertex_indexes.append(new_graph.vertex.index(vertex))
        self.assertEqual(weak_vertex_indexes, [])

    def test_find_weak_nodex_square(self):
        new_graph = SimpleGraph(4)

        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))
        new_graph.AddVertex(randint(0, 100))

        new_graph.AddEdge(0, 1)
        new_graph.AddEdge(0, 2)
        new_graph.AddEdge(1, 3)
        new_graph.AddEdge(2, 3)

        weak_vertex_indexes = []
        for vertex in new_graph.WeakVertices():
            weak_vertex_indexes.append(new_graph.vertex.index(vertex))
        self.assertEqual(weak_vertex_indexes, [0, 1, 2, 3])

    def tearDown(self):
        pass


unittest.main()
