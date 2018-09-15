def sorting3(step, data):
    """  Алгоритм проходит по всем элементам массива"""
    circle = 1
    while circle <= step:
        for index in range(circle, len(data), step):
            currentvalue = data[index]
            position = index
            while position > 0 and data[position - step] > currentvalue:
                data[position] = data[position - step]
                position = position - step
            data[position] = currentvalue
        circle +=1
    return data


a = [7, 6, 5, 4, 3, 2, 1]

print(sorting3(3, a))

