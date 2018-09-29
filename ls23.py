import random

class KsortedArray:

    def __init__(self):
        self.array = {}

    def hash_fun(self, value):
        return id(value)%10

    def put(self, value):
        hash = self.hash_fun(value)
        if hash in self.array:
            self.array[hash].append(value)
            return
        self.array[hash] = [value]

    def get_key(self,value):
        hash = self.hash_fun(value)
        if hash in self.array:
            for i in range(len(self.array[hash])):
                if self.array[hash][i] == value:
                    return hash,i
            return False
        return False


letters = 'abcdefgh'
b = KsortedArray()

for elem in range(20):
    elem = letters[random.randint(0, 7)] + str(random.randint(0,100)%10) + str(random.randint(0,100)%10)
    b.put(elem)

for i in b.array:
    print(i, b.array[i])