import random, timeit


def separ(lst, start, end):
    pos = start
    ref = lst[start]
    for i in range(start, end+1):
        if lst[i] <= ref:
            lst[i], lst[pos] = lst[pos], lst[i]
            pos += 1
    pos -= 1
    lst[pos], lst[start] = lst[start], lst[pos]
    return pos


def quicksort(lst, start, end):
    if start < end:
        pos = separ(lst, start, end)
        quicksort(lst, start, pos - 1)
        quicksort(lst, pos + 1, end)


def shell_sort(data):
    step = 1
    while (3 * step) + 1 < len(data):
        step = (3 * step) +1
    while step > 0:
        for index in range(1, len(data), step):
            current_value = data[index]
            position = index
            while position - step  >= 0 and data[position - step] > current_value:
                data[position] = data[position - step]
                position = position - step
            data[position] = current_value
        step = step // 3
    return data


big_arr_quicksort = [random.random() for i in range(10000)]
big_arr_shell = [random.random() for i in range(10000)]
big_arr_p_sort = [random.random() for i in range(10000)]

t1 = timeit.Timer(lambda: quicksort(big_arr_quicksort, 0, len(big_arr_quicksort)-1)).timeit(number=1)
t2 = timeit.Timer(lambda: shell_sort(big_arr_shell)).timeit(number=1)
t3 = timeit.Timer(lambda: big_arr_p_sort.sort()).timeit(number=1)

print('Quicksort time',t1)
print('Shell sort time',t2)
print('Standart sort time',t3)

