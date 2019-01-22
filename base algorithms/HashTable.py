class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.count = 0

    def hash_fun(self, value):
        return id(value) % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        if self.count >= self.size:
            return None
        while True:
            if self.slots[slot] is None:
                return str(slot)
            slot = (slot + self.step) % self.size

    def put(self, value):
        if self.seek_slot(value):
            free_slot = int(self.seek_slot(value))
            self.slots[free_slot] = value
            self.count += 1
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
