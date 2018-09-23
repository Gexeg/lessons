import random

class PresortArray:
    def __init__(self, arr):
        self.array = arr
        self.avg = sum(arr)/len(arr)

def array_s(list_in, list_avg):
    if len(list_in) == 1:
        return False
    result = list_in
    start_i = 0
    end_i = len(result) - 1
    while start_i != end_i - 1:
        if result[start_i] <= list_avg:
            start_i += 1
            continue
        if result[end_i] > list_avg:
            end_i -= 1
        result[start_i], result[end_i] = result[end_i], result[start_i]
    step = 1
    while (3 * step) + 1 < len(result):
        step = (3 * step) +1
    while step > 0:
        for index in range(1, len(result), step):
            current_value = result[index]
            position = index
            while position - step  >= 0 and result[position - step] > current_value:
                result[position] = result[position - step]
                position = position - step
            result[position] = current_value
        step = step // 3
    return result

a = []
for i in range(random.randint(1,5)):
    a.append(random.randint(0,15))
a = PresortArray(a)

print(a.array)
print(array_s(a.array, a.avg))
