import random, timeit

class Heap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_node_index = 0
        self.storage = [None] * capacity

    def add_node(self, value, array_index):
        if self.last_node_index == self.capacity:
            return None
        new_node = Node(value, array_index)
        current_ind = self.last_node_index
        self.storage[self.last_node_index] = new_node
        self.last_node_index += 1
        while current_ind != 0:
            new_node_value = self.storage[current_ind].value
            parent_node_value = self.storage[(current_ind - 1) // 2].value
            parent_node_index = (current_ind - 1) // 2
            if new_node_value < parent_node_value:
                break
            if new_node_value > parent_node_value:
                self.swap(current_ind, parent_node_index)
            current_ind = parent_node_index

    def pop(self):
        """Получение корня"""
        if self.storage[0]:
            pop = self.storage[0]
        else:
            return None
        self.storage[0] = self.storage[self.last_node_index-1]
        self.storage[self.last_node_index-1] = None
        self.last_node_index -= 1
        current_ind = 0
        while True:
            r_child_index = current_ind * 2 + 2 if current_ind * 2 + 2 < len(self.storage) - 1 else None
            if r_child_index:
                r_child_value = self.storage[r_child_index].value if self.storage[r_child_index] else None
            else:
                r_child_value = None
            l_child_index = current_ind * 2 + 1 if current_ind * 2 + 1 < len(self.storage) - 1 else None
            if l_child_index:
                l_child_value = self.storage[l_child_index].value if self.storage[l_child_index] else None
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
            if self.storage[current_ind].value < max_child_value:
                self.swap(current_ind, max_child_ind)
                current_ind = max_child_ind
            else:
                return pop

    def swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
        return


class Node:
    def __init__(self, value, array_index):
        self.value = value
        self.array_index = array_index

def merge_sort(array, k):
    if len(array) > 1:
        step = len(array)//k if len(array)//k > 0 else 1
        slices = [array[i:i + step] for i in range(0, len(array), step)]
        for chunk in slices:
            merge_sort(chunk, k)
        heap = Heap(len(slices))

        chunk_index = 0
        for chunk in slices:
            heap.add_node(chunk.pop(0), chunk_index)
            chunk_index += 1

        k = 0
        while True:
            result = heap.pop()
            if result is None:
                break
            value = result.value
            chunk_index = result.array_index
            array[k] = value
            k += 1
            if len(slices[chunk_index]) > 0:
                heap.add_node(slices[chunk_index].pop(0), chunk_index)


big_arr_merge2 = [random.random() for i in range(10000)]
big_arr_merge16 = [random.random() for i in range(10000)]
big_arr_p_sort = [random.random() for i in range(10000)]

t1 = timeit.Timer(lambda: merge_sort(big_arr_merge2, 2)).timeit(number=1)
t2 = timeit.Timer(lambda: merge_sort(big_arr_merge16, 16)).timeit(number=1)
t3 = timeit.Timer(lambda: big_arr_p_sort.sort()).timeit(number=1)

print('Merge time (k = 2)',t1)
print('Merge time (k = 16)',t2)
print('Standart sort time',t3)
print()
print('Test array')
test_arr = [random.randint(0,1) for i in range(15)]
print(test_arr)
merge_sort(test_arr, 4)
print('_____________')
print(test_arr)