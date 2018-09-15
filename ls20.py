def sorting2(step, data):
    """  Алгоритм не сортирует список полностью, он лишь 1 раз проходит по списку с заданным шагом"""
    for index in range(1, len(data)):
        if index % step == 0:
            currentvalue = data[index]
            position = index
            while position > 0 and data[position - step] > currentvalue:
                data[position] = data[position - step]
                position = position - step
            data[position] = currentvalue
    return data


a = [7, 6, 5, 4, 3, 2, 1]

print(sorting2(3, a))

