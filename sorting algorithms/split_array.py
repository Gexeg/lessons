import random

def array_s(list_in):
    if len(list_in) == 1:
        return False
    result = list_in
    list_avg = sum(result) / len(result)
    start_i = 0
    end_i = len(result) - 1
    while start_i != end_i - 1:
        if result[start_i] <= list_avg:
            start_i += 1
            continue
        if result[end_i] > list_avg:
            end_i -= 1
        result[start_i], result[end_i] = result[end_i], result[start_i]
    return start_i, end_i


a = []

for i in range(random.randint(1,20)):
    a.append(random.randint(0,1))

print(a)
print(array_s(a))

