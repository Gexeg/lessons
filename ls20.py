import random

def shell_sort(data):
    """  Алгоритм проходит по всем элементам массива"""
    print('Сгенерированный массив')
    print(data)
    print()
    print('Шаги сортировки')
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
        print(step)
        step = step // 3
    print()
    print('Отсортированный массив')
    return data

a = []

for i in range(random.randint(1,20)):
    a.append(random.randint(0,100))

print(shell_sort(a))

