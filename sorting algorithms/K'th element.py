import random

def find_k(array, k):
    left = 0
    right = len(array) - 1
    while True:
        pos = separ(array, left, right)
        if pos == k:
            return array[pos]
        elif k < pos:
            right = pos - 1
        else:
            left = pos + 1

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

a = [random.randint(0,100) for i in range(10 )]

print('Сгенерированный массив')
print(a)
k = 8
b = find_k(a, k)
print('К\'элемент = ', b)
a.sort()
print()
print('Отсортированный массив(для удобства проверки)')
print('Искомый элемент {}'.format(k))
print(a, b)
