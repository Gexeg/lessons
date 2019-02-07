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
    while start < end:
        pos = separ(array, start, end)
        if pos - start < end - pos:
            quicksort(array, start, pos - 1)
            start = pos + 1
        else:
            quicksort(array, pos + 1, end)
            end = pos - 1

arr = [0,213,454,648,4,34,3213,44,8,7,9,9,1,3,5,7,8,0,45]
quicksort(arr, 0, len(arr) - 1 )
print(arr)

big_arr_quicksort = [random.random() for i in range(10000)]
big_arr_p_sort = [random.random() for i in range(10000)]

t1 = timeit.Timer(lambda: quicksort(big_arr_quicksort, 0, len(big_arr_quicksort)-1)).timeit(number=1)
t3 = timeit.Timer(lambda: big_arr_p_sort.sort()).timeit(number=1)

print('Quicksort time',t1)
print('Standart sort time',t3)

