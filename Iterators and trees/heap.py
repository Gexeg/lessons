class Heap:

    def __init__(self):
        self.HeapArray = []# хранит неотрицательные числа-ключи

    def MakeHeap(self, a):
        self.HeapArray = [None] * len(a)
        for key in a:
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
        while True:
            r_child_index = current_ind * 2 + 2 if current_ind * 2 + 2 < len(self.HeapArray) - 1 else None
            if r_child_index:
                r_child_value = self.HeapArray[r_child_index] if self.HeapArray[r_child_index] else None
            else:
                r_child_value = None
            l_child_index = current_ind * 2 + 1 if current_ind * 2 + 1 < len(self.HeapArray) - 1 else None
            if l_child_index:
                l_child_value = self.HeapArray[l_child_index] if self.HeapArray[l_child_index] else None
            else:
                l_child_value = None
            if r_child_value and l_child_value:
                if r_child_value > l_child_value:
                    max_child_ind = r_child_index
                    max_child_value = r_child_value
                else:
                    max_child_ind = l_child_index
                    max_child_value = l_child_value
            elif r_child_value:
                max_child_ind = r_child_index
                max_child_value = r_child_value
            elif l_child_value:
                max_child_ind = l_child_index
                max_child_value = l_child_value
            else:
                return pop
            if self.HeapArray[current_ind] < max_child_value:
                self.swap(current_ind, max_child_ind)
                current_ind = max_child_ind
            else:
                return pop

    def swap(self, i, j):
        self.HeapArray[i], self.HeapArray[j] = self.HeapArray[j], self.HeapArray[i]
        return
