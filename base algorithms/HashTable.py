import unittest

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.collision_counter = 0

    def hash_fun(self, value):
        return id(value) % self.size

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


h_table = HashTable(10000, 55)
for num in range(10000):
    h_table.put('Hash' + str(num))
print(h_table.collision_counter)