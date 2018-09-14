def sorting(step,data):
    for index in range(1, len(data)):
        if index % step == 0:
            currentvalue = data[index]
            position = index
            while position > 0 and data[position - 1] > currentvalue:
                data[position] = data[position - 1]
                position = position - 1
            data[position] = currentvalue
    return data


a = [7,6,5,4,3,2,1]

print(sorting(3,a))
