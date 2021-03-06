import unittest
from random import choice


class Heap:

    def __init__(self):
        self.HeapArray = []# хранит неотрицательные числа-ключи

    def MakeHeap(self, array):
        new_tree_capacity = 0
        tree_depth = 0
        while new_tree_capacity < len(array):
            tree_depth += 1
            new_tree_capacity = (2 ** (tree_depth + 1)) - 1
        self.HeapArray = [None] * new_tree_capacity
        for key in array:
            self.Add(key)

    def Add(self, key):
        """добавление нового элемента"""
        None_ind = next((i for i, x in enumerate(self.HeapArray) if x is None), False)
        if None_ind is False:
            return False
        current_ind = None_ind
        self.HeapArray[None_ind] = key
        while current_ind != 0:
            parent_node_index = (current_ind - 1) // 2
            new_node_value = self.HeapArray[current_ind]
            parent_node_value = self.HeapArray[(current_ind - 1) // 2]
            if new_node_value < parent_node_value:
                break
            if new_node_value > parent_node_value:
                self.swap(current_ind, parent_node_index)
            current_ind = parent_node_index
        return True

    def GetMax(self):
        """Получение корня"""
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1
        none_ind = next((i - 1 for i, x in enumerate(self.HeapArray) if x is None), len(self.HeapArray)-1)
        pop = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[none_ind]
        self.HeapArray[none_ind] = None
        current_ind = 0
        current_value = self.HeapArray[0]
        while True:
            max_child_ind_value = self.find_max_child(current_ind)
            if max_child_ind_value:
                if current_value < max_child_ind_value[1]:
                    self.swap(current_ind, max_child_ind_value[0])
                    current_ind = max_child_ind_value[0]
                else:
                    return pop

            else:
                return pop

    def find_max_child(self, current_ind):
        max_index = len(self.HeapArray) - 1
        r_child_ind = current_ind * 2 + 2
        l_child_ind = current_ind * 2 + 1

        r_child_value = self.HeapArray[r_child_ind] if r_child_ind <= max_index else None
        l_child_value = self.HeapArray[l_child_ind] if l_child_ind <= max_index else None

        if r_child_value and l_child_value:
            if r_child_value > l_child_value:
                return r_child_ind, r_child_value
            if l_child_value > r_child_value:
                return l_child_ind, l_child_value
        if r_child_value:
            return r_child_ind, r_child_value
        if l_child_value:
            return l_child_ind, l_child_value

    def swap(self, i, j):
        self.HeapArray[i], self.HeapArray[j] = self.HeapArray[j], self.HeapArray[i]



class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_make_heap(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_empty_heap_add(self):
        new_heap = Heap()
        self.assertEqual(new_heap.Add(15), False)

    def test_make_heap_2(self):
        array = [10, 15, 37, 22, 56, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        array2 = [10, 15, 6, 22, 34, 86]
        new_heap.MakeHeap(array2)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)


    def test_GetMax(self):
        array = [10, 15, 37, 22, 56, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        roots = [86, 56, 37, 22, 15, 10]
        for ind in range(6):
            self.assertEqual(new_heap.GetMax(), roots[ind])
        empty_array = [None] * 7
        self.assertEqual(len(new_heap.HeapArray), 7)
        self.assertEqual(new_heap.HeapArray, empty_array)

    def test_GetMax_make_new(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        for key in array:
            self.assertEqual(new_heap.GetMax() is not None, True)
            self.assertEqual(len(new_heap.HeapArray), 7)
        new_heap.MakeHeap(array)
        self.assertEqual(len(new_heap.HeapArray), 7)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_make_new2(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        for key in range(3):
            self.assertEqual(new_heap.GetMax() is not None, True)
        new_heap.MakeHeap(array)
        self.assertEqual(len(new_heap.HeapArray), 7)
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_make_new3(self):
        array = [10]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        self.assertEqual(new_heap.GetMax(), 10)
        self.assertEqual(new_heap.HeapArray, [None, None, None])
        new_heap.MakeHeap(array)
        self.assertEqual(len(new_heap.HeapArray), 3)
        etalon_array = [10, None, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_Add(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        for key in range(8):
            self.assertEqual(new_heap.GetMax() is not None, True)
        for i in range(6):
            new_heap.Add(array[i])
        etalon_array = [86, 22, 34, 10, 15, 6, None]
        self.assertEqual(new_heap.HeapArray, etalon_array)

    def test_GetMax_Add2(self):
        array = [10, 15, 6, 22, 34, 86, 5]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        for i in range(6):
            self.assertEqual(new_heap.Add(array[i]), False)
        etalon_array = [86, 22, 34, 10, 15, 6, 5]
        self.assertEqual(new_heap.HeapArray, etalon_array)


    def test_GetMax_Add3(self):
        array = [10, 15, 6, 22, 34, 86]
        new_heap = Heap()
        new_heap.MakeHeap(array)
        for i in range(82):
            self.assertEqual(new_heap.GetMax() is not None, True)
            self.assertEqual(len(new_heap.HeapArray), 7)
            self.assertEqual(new_heap.Add(choice(array)), True)
        self.assertEqual(len(new_heap.HeapArray), 7)

    def tearDown(self):
        pass


unittest.main()

