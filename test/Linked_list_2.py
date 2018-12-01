class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        if self.tail:
            if self.tail.value == val:
                return self.tail
        return None

    def find_all(self, val):
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)
            node = node.next
        return node_list

    def delete(self, val, all=False):
        if all:
            while self.find(val):
                self.delete(val)
        node = self.find(val)
        if node:
            if self.head.value == val:
                if self.len() <= 1:
                    self.clean()
                    return
                self.head = self.head.next
                self.head.prev = None
                return
            if node == self.tail and node != None:
                self.tail.prev.next = None
                self.tail = self.tail.prev
                return
            node.next.prev = node.prev
            node.prev.next = node.next
            return
        return False


    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.len() == 0:
                self.add_in_tail(newNode)
                return True
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                return True
        else:
            node = self.find(afterNode)
            if node == self.tail and node != None:
                node.next = newNode
                newNode.prev = node
                self.tail = newNode
                return
            if node:
                newNode.prev = node
                newNode.next = node.next
                node.next.prev = newNode
                node.next = newNode
                return True
        return False

    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
