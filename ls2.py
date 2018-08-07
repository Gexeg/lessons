import unittest

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

    def add_in_head(self, item):
        """Задание номер 3 метод для помещения узла в голову списка"""
        if self.tail is None:
            self.tail = item
            item.prev = None
            item.next = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

    def find_and_del(self, val):
        """Задание номер 1 метод для поиска и удаления узла по значению"""
        node = self.head
        started = True
        while node is not None:
            if started== True:
                if node.value == val:
                    self.head = node.next
                    node.next.prev = None
                    return
                started = False
            if node.value == val:
                node.next.prev = node.prev
                node.prev.next = node.next
                return
            node = node.next
        return False

    def find_and_paste(self, find_val, node_val):
        """Задание номер 2 метод для помещения узла после заданного узла"""
        node = self.head
        node_for_paste = Node(node_val)
        while node is not None:
            if node.value == find_val:
                node_for_paste.prev = node
                node_for_paste.next = node.next
                node.next.prev = node_for_paste
                node.next = node_for_paste
                return
            node = node.next
        return False

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
        return None

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght



list2 = LinkedList2()
list2.add_in_tail(Node(12))
list2.add_in_tail(Node(124))
list2.add_in_tail(Node(1))
list2.add_in_tail(Node(19))
list2.add_in_tail(Node(22))
list2.add_in_tail(Node(8937))

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_in_head(self):
        list2.add_in_head(Node(123))
        self.assertEqual(list2.len(), 7)

    def test_find_and_del(self):
        list2.find_and_del(19)
        self.assertEqual(list2.len(), 6)

    def test_find_and_paste(self):
        list2.find_and_paste(19, 44)
        self.assertEqual(list2.len(), 6)

    def tearDown(self):
        pass

unittest.main()

