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
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0

    def add(self, num):
        node_for_add = Node(num)
        node = self.head
        if self.head is None:
            self.head = node_for_add
            node_for_add.prev = None
            node_for_add.next = None
            self.tail = node_for_add
            return
        else:
            if self.get_asc():
                if self.compare(num, self.tail.value) >= 0:
                    node_for_add.next = None
                    node_for_add.prev = self.tail
                    self.tail.next = node_for_add
                    self.tail = node_for_add
                    return
                elif self.compare(self.head.value, num ) >= 0:
                    self.head.prev = node_for_add
                    node_for_add.next = self.head
                    self.head = node_for_add
                    node_for_add.prev = None
                    return
                else:
                    while node != None:
                        if self.compare(node.value, num) >= 0:
                            node_for_add.prev = node.prev
                            node_for_add.next = node
                            node.prev.next = node_for_add
                            node.prev = node_for_add
                            return
                        node = node.next
            else:
                if self.compare(self.tail.value, num) >= 0:
                    node_for_add.next = None
                    node_for_add.prev = self.tail
                    self.tail.next = node_for_add
                    self.tail = node_for_add
                    return
                elif self.compare(num, self.head.value) >= 0:
                    self.head.prev = node_for_add
                    node_for_add.next = self.head
                    self.head = node_for_add
                    node_for_add.prev = None
                    return
                else:
                    while node != None:
                        if self.compare(num, node.value) >= 0:
                            node_for_add.prev = node.prev
                            node_for_add.next = node
                            node.prev.next = node_for_add
                            node.prev = node_for_add
                            return
                        node = node.next

    def find(self, value):
        node = self.head
        if self.get_asc():
            while node != None:
                if value < node.value:
                    return None
                if value == node.value:
                    return node
                node = node.next
        else:
            while node != None:
                if value > node.value:
                    return None
                if value == node.value:
                    return node
                node = node.next

    def delete(self, val):
        node = self.head
        started = True
        while node is not None:
            if started == True:
                if node.value == val:
                    self.head = node.next
                    if node.next:
                        node.next.prev = None
                    return
                started = False
            if node.value == val:
                node.next.prev = node.prev
                node.prev.next = node.next
                return
            node = node.next
        return False

    def clean(self):
        self.head = None
        self.tail = None
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
        if len(v1.strip()) < len(v2.strip()):
            return -1
        elif len(v1.strip()) > len(v2.strip()):
            return 1
        else:
            return 0

