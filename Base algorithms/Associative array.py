class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
         slot = id(str(key)) % self.size
         marked_slots = 0
         while True:
             if self.slots[slot] is None or self.slots[slot] == key:
                 return slot
             slot = (slot + 1) % self.size
             marked_slots += 1
             if marked_slots > self.size:
                 return None

    def is_key(self, key):
         slot = self.hash_fun(key)
         marked_slots = 0
         if slot or slot == 0:
             while True:
                 if self.slots[slot] == key:
                     return True
                 slot = (slot + 1) % self.size
                 marked_slots += 1
                 if marked_slots == self.size:
                     return False

    def put(self, key, value):
         slot = self.hash_fun(key)
         if slot or slot == 0:
             self.slots[slot] = key
             self.values[slot] = value
         return

    def get(self, key):
         if self.is_key(key):
             slot = self.hash_fun(key)
             marked_slots = 0
             while True:
                 if self.slots[slot] == key:
                     return self.values[slot]
                 slot = (slot + 1) % self.size
                 marked_slots += 1
                 if marked_slots > self.size:
                     return None
         return None