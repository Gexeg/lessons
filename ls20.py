def sorting3(step, data):
    """  Алгоритм проходит по всем элементам массива"""
    circle = 0
    while circle < step:
        for index in range(circle, len(data), step):
            current_value = data[index]
            position = index
            print(circle, ' circ')
            print(position, ' pos')
            print(current_value,  ' cur')
            while position - step  >= 0 and data[position - step] > current_value:
                data[position] = data[position - step]
                position = position - step
            data[position] = current_value
            print(data)
            print()
        circle +=1
    return data


a = [1, 6, 5, 7, 3, 2, 4]

print(sorting3(3, a))

