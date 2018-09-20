import random

def array_s(list_in):
    result = list_in
    list_avg = int(sum(result) / len(result))
    start_i = 0
    end_i = len(result) - 1
    while start_i != end_i - 1:
        if start_i == end_i or start_i > end_i:
            break
        if result[start_i] <= list_avg:
            start_i += 1
        if result[end_i] >= list_avg:
            end_i -= 1
        result[start_i], result [end_i] = result[end_i], result[start_i]

    return result, list_avg


a = []

for i in range(random.randint(1,20)):
    a.append(random.randint(0,100))

print(a)
print(array_s(a))

