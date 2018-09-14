def sorting(step,data):
    for index in range(1, len(data)):
        if index % step == 0:
            currentvalue = data[index]
            while index > 0 and data[index - 1] > currentvalue:
                data[index] = data[index - 1]
                index = index - 1
            data[index] = currentvalue
    return data


a = [7,6,5,4,3,2,1]

print(sorting(3,a))

