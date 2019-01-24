class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return id(value) % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        visited_slots = 0
        while True:
            if self.slots[slot] is None:
                return slot
            slot = (slot + self.step) % self.size
            visited_slots += 1
            if visited_slots > self.size:
                return None

    def put(self, value):
        if self.seek_slot(value) or self.seek_slot(value) == 0:
            free_slot = self.seek_slot(value)
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
