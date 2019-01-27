from random import randint

class HashTable:
    def __init__(self, sz, stp, fun_amount = 3, curr_coeff = 0):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.hf_fun = lambda value, a, b, p: (((a * id(value)) + b) % p) % self.size
        self.coeff_roster = self.generate_coefficients(fun_amount)
        """В рамках теста функции выбираются вручную, чтобы можно было
        посмотреть сразу все семейство. В общем случае выбирается одна функция из семейства
        self.curr_coeff = randint(0, len(self.coeff_roster) - 1)"""
        self.curr_coeff = curr_coeff
        self.collision_counter = 0

    def hash_fun(self, value):
        curr_coeff = self.coeff_roster[self.curr_coeff]
        return self.hf_fun(value, curr_coeff[0], curr_coeff[1], curr_coeff[2])

    def generate_coefficients(self, fun_amount):
        prime_num = []
        a = 0
        num = self.size + 1
        while a != fun_amount:
            for elem in range(2, num):
                if (num % elem) == 0:
                    num += 1
                    break
                else:
                    a += 1
                    prime_num.append(num)
                    num += 1
                    break
        coeff = []
        for p in prime_num:
            a = randint(1, p - 1 )
            b = randint(0, p - 1)
            coeff.append([a, b, p])
        return coeff

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        visited_slots = 0
        collision = False
        while True:
            if self.slots[slot] is None:
                return slot
            if collision is False:
                self.collision_counter += 1
                collision = True
            slot = (slot + self.step) % self.size
            visited_slots += 1
            if visited_slots > self.size:
                return None

    def put(self, value):
        free_slot = self.seek_slot(value)
        if free_slot or free_slot == 0:
            self.slots[free_slot] = value
            return free_slot
        return None

    def find(self, value):
        slot = self.hash_fun(value)
        marked_slots = 0
        while True:
            if self.slots[slot] == value:
                return slot
            slot = (slot + self.step) % self.size
            marked_slots += 1
            if marked_slots == self.size:
                return None


stats = {}
for i in range(3):
    h_table = HashTable(10000, 55, 3, i)
    for num in range(10000):
        h_table.put('Hash' + str(num))
    stats[str(h_table.coeff_roster[h_table.curr_coeff])] = h_table.collision_counter

print('Длина таблицы: 10000, шаг: 55')
for key, val in stats.items():
    print('Используемые коэффициенты и простое число(a,b,p): ',key,' Количество коллизий:',val)