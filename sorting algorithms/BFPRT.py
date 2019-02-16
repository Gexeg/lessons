import random

def find_k(array, k):
    pivot = find_pivot(array)
    low_elements = [element for element in array if element < pivot]
    highs_elements = [element for element in array if element > pivot]
    pivots = [element for element in array if element == pivot]
    if k < len(low_elements):
        return find_k(low_elements, k)
    elif k < len(low_elements) + len(pivots):
        return pivots[0]
    else:
        return find_k(highs_elements, k - len(low_elements) - len(pivots))

def find_pivot(array):
    slices = slice_array(array)
    for element in slices:
        sort_array(element)
    medians = [find_median(arr) for arr in slices]
    medians.sort()
    main_median = find_median(medians)
    return main_median

def slice_array(array):
    return [array[i:i + 5] for i in range(0, len(array), 5)]

def sort_array(array):
    return array.sort()

def find_median(array):
    if len(array) % 2 == 1:
        return array[len(array)//2]
    else:
        return (array[len(array)//2-1] + array[len(array)//2])//2

a = [random.randint(0,100) for i in range(10)]
b = find_k(a, 3)
print(a)
print(b)