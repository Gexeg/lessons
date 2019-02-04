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
        self.current = None

    def __next__(self):
        node = self.current
        try:
            self.current = self.current.next
        except:
            raise StopIteration
        return node

    def __iter__(self):
        return self

    def first(self):
        self.current = self.head
        return

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.current = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
        return

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_and_del(self, val):
        node = self.head
        started = True
        while node is not None:
            if started== True:
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
        return 'Узел не найден'

    def find_all_and_del(self, val):
        node = self.head
        started = True
        while node is not None:
            if started:
                if node.value == val:
                    self.head = node.next
                started = False
                previos_node = node
            if node.value == val:
                previos_node.next = node.next
            previos_node = node
            node = node.next
        self.find_and_del(val)
        return

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

    def find_all(self, val):
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)
            node = node.next
        return node_list

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def find_and_paste(self, val, node_val):
        node = self.head
        node_for_paste = Node(node_val)
        while node is not None:
            if node.value == val:
                node_for_paste.next = node.next
                node.next = node_for_paste
                return
            node = node.next
        return  False

s_list = LinkedList()
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(125))

for i in s_list:
    print(i.value)