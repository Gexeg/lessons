class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def get_asc(self):
        return self.__ascending

    def change_asc(self):
        if self.get_asc():
            self.__ascending = False
        else:
            self.__ascending = True

    def compare(self, v1, v2):
        if self.get_asc():
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            else:
                return 0
        else:
            if v1 < v2:
                return 1
            elif v1 > v2:
                return -1
            else:
                return 0

    def add(self, num):
        node_for_add = Node(num)
        if self.head is None:
            self.head = node_for_add
            self.tail = node_for_add
            return
        if self.compare(num, self.tail.value) >= 0:
            node_for_add.next = None
            node_for_add.prev = self.tail
            self.tail.next = node_for_add
            self.tail = node_for_add
            return
        if self.compare(self.head.value, num) >= 0:
            self.head.prev = node_for_add
            node_for_add.next = self.head
            self.head = node_for_add
            node_for_add.prev = None
            return
        node = self.head
        while node != None:
            if self.compare(node.value, num) >= 0:
                node_for_add.prev = node.prev
                node_for_add.next = node
                node.prev.next = node_for_add
                node.prev = node_for_add
                return
            node = node.next

    def find(self, value):
        node = self.head
        while node != None:
            if self.compare(node.value, value) > 0:
                return None
            elif node.value == value:
                return node
            node = node.next

    def delete(self, val):
        node = self.find(val)
        if node:
            if node == self.head:
                if self.len() == 1:
                    self.head = None
                    self.tail = None
                    return
                self.head = self.head.next
                self.head.prev = None
                return
            if node == self.tail:
                self.tail.prev.next = None
                self.tail = self.tail.prev
                return
            node.next.prev = node.prev
            node.prev.next = node.next
            return
        return False

    def clean(self, change_asc = False):
        self.head = None
        self.tail = None
        if change_asc:
            self.change_asc()

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def get_asc(self):
        return self.__ascending

    def change_asc(self):
        if self.get_asc():
            self.__ascending = False
        else:
            self.__ascending = True

    def compare(self, v1, v2):
        if self.get_asc():
            if len(v1.strip()) < len(v2.strip()):
                return -1
            elif len(v1.strip()) > len(v2.strip()):
                return 1
            else:
                return 0
        else:
            if len(v1.strip()) < len(v2.strip()):
                return 1
            elif len(v1.strip()) > len(v2.strip()):
                return -1
            else:
                return 0
