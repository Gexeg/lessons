class PowerSet:

    def __init__(self):
        self.slots = []

    def put(self, value):
        if value not in self.slots:
            self.slots.append(value)

    def get(self, value):
        return value in self.slots

    def remove(self, value):
        if value in self.slots:
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        for i in self.slots:
            for y in set2.slots:
                if i == y:
                    result.put(i)
        return result

    def union(self, set2):
        result = PowerSet()
        for i in self.slots:
            result.put(i)
        for y in set2.slots:
            result.put(y)
        return result

    def difference(self, set2):
        result = PowerSet()
        for element in self.slots:
            if set2.get(element) is False:
                result.put(element)
        return result

    def issubset(self, set2):
        counter = 0
        for i in set2.slots:
            if i in self.slots:
                counter +=1
        return counter == len(set2.slots)

