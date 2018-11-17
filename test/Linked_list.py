class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def description(self):
        print(self.value)
        print(self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        if self.tail:
            if self.tail.value == val:
                return val
        return None

    def find_all(self, val):
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)
            node = node.next
        if self.tail:
            if self.tail.value == val:
                node_list.append(self.tail)
        return node_list

    def delete(self, val, all = False):
        node = self.head
        started = True
        if all:
            while self.find(val):
                self.delete(val)
        else:
            while node is not None:
                if started == True:
                    if node.value == val:
                        self.head = node.next
                        return
                    started = False
                    previos_node = node
                if node.value == val:
                    previos_node.next = node.next
                    return
                previos_node = node
                node = node.next
            if self.tail.value == val:
                if self.head:
                    self.tail = previos_node
                else:
                    self.tail = None

    def clean(self):
        node = self.head
        started = True
        while node is not None:
            if started == True:
                started = False
                previos_node = node
            previos_node.next = None
            previos_node = node
            node = node.next
        self.head = None
        self.tail = None
        return None

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def insert(self, val, node_val):
        node = self.head
        node_for_paste = Node(node_val)
        while node is not None:
            if node.value == val:
                node_for_paste.next = node.next
                node.next = node_for_paste
                return True
            node = node.next
        return False