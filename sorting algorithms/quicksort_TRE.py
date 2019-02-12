import random, timeit


def separ(array, start, end):
    pos = start
    ref = array[start]
    for i in range(start, end+1):
        if array[i] <= ref:
            array[i], array[pos] = array[pos], array[i]
            pos += 1
    pos -= 1
    array[pos], array[start] = array[start], array[pos]
    return pos


def quicksort(array, start, end):
    if start < end:
        position = separ(array, start, end)
        if position - start > end - position:
            stack = []
            stack.append(start)
            stack.append(position - 1)
            while len(stack) > 0:
                wh_end = stack.pop()
                wh_start = stack.pop()
                pos = separ(array, wh_start, wh_end)
                if pos - 1 > wh_start:
                    stack.append(wh_start)
                    stack.append(pos-1)
                if pos + 1 < wh_end:
                    stack.append(pos + 1)
                    stack.append(wh_end)
            return quicksort(array, position + 1, end)
        else:
            stack = []
            stack.append(position + 1)
            stack.append(end)
            while len(stack) > 0:
                wh_end = stack.pop()
                wh_start = stack.pop()
                pos = separ(array, wh_start, wh_end)
                if pos - 1 > wh_start:
                    stack.append(wh_start)
                    stack.append(pos - 1)
                if pos + 1 < wh_end:
                    stack.append(pos + 1)
                    stack.append(wh_end)
            return quicksort(array, position + 1, end)

arr = [1,10,5,9,0, 1293,1023,0,12]

quicksort(arr, 0, len(arr) - 1)
print(arr)

big_arr_quicksort = [random.random() for i in range(1000)]
big_arr_p_sort = [random.random() for i in range(1000)]

t1 = timeit.Timer(lambda: quicksort(big_arr_quicksort, 0, len(big_arr_quicksort)-1)).timeit(number=1)
t3 = timeit.Timer(lambda: big_arr_p_sort.sort()).timeit(number=1)

print('Quicksort time',t1)
print('Standart sort time',t3)