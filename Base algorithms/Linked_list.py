import unittest

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

    def delete(self, val, all = False):
        node = self.head
        started = True
        if all:
            while self.find(val):
                self.delete(val)
        else:
            while node:
                if started == True:
                    if node.value == val:
                        if self.len() <= 1:
                            self.clean()
                            return
                        self.head = node.next
                        return
                    started = False
                    previos_node = node
                if node.value == val:
                    previos_node.next = node.next
                    return
                previos_node = node
                node = node.next
            if self.tail:
                if self.tail.value == val:
                    if self.head:
                        self.tail = previos_node
                    else:
                        self.tail = None

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

    def insert(self, afterNode, new_node):
        node = self.head
        if afterNode is None:
            if self.len() == 0:
                self.add_in_tail(new_node)
                return True
        while node is not None:
            if node == afterNode:
                new_node.next = node.next
                node.next = new_node
                if self.tail:
                    if self.tail == afterNode:
                        new_node.next = None
                        self.tail.next = new_node
                        self.tail = new_node
                return True
            node = node.next
        return False


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_delete_all_nodes(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.delete(125, True)
        self.assertEqual(s_list.find(125), None)
        self.assertEqual(s_list.print_all_nodes(), None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(s_list.head, None)

    def test_delete_all_nodes_in_one_element_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(125))
        s_list.delete(125, True)
        self.assertEqual(s_list.find(125), None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(s_list.head, None)

    def test_delete_all_various_nodes(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(45))
        s_list.add_in_tail(Node(165))
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(125))
        s_list.delete(125, True)
        self.assertEqual(s_list.find(125), None)
        self.assertEqual(s_list.head.value, 45)
        self.assertEqual(s_list.tail.value, 12)

    def test_delete_all_various_nodes_one_head(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(125))
        s_list.delete(125, True)
        self.assertEqual(s_list.tail.value, 175)
        self.assertEqual(s_list.head.value, 175)

    def test_delete_node_single_node(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(175))
        s_list.delete(175)
        self.assertEqual(s_list.find(175), None)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_delete_node(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(175))
        s_list.delete(175)
        self.assertEqual(len(s_list.find_all(175)), 3)
        self.assertEqual(s_list.head.value, 175)
        self.assertEqual(s_list.tail.value, 175)

    def test_delete_node_empty_list(self):
        s_list = LinkedList()
        s_list.delete(175)
        self.assertEqual(len(s_list.find_all(175)), 0)


    def test_find(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(125))
        self.assertEqual(s_list.find(125), s_list.tail)

    def test_find_none(self):
        s_list = LinkedList()
        self.assertEqual(s_list.find(125), None)

    def test_insert(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(175))
        self.assertEqual(s_list.insert(s_list.find(175), Node(125)), True)
        self.assertEqual(s_list.find(125).value, 125)
        self.assertEqual(s_list.tail.value, 125)

    def test_insert_3(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(145))
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(175))
        self.assertEqual(s_list.insert(s_list.find(175), Node(125)), True)
        self.assertEqual(s_list.find(125).value, 125)
        self.assertEqual(s_list.tail.value, 125)

    def test_insert_2(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(5))
        self.assertEqual(s_list.insert(s_list.find(175), Node(125)), False)

    def test_insert_empty_list(self):
        s_list = LinkedList()
        self.assertEqual(s_list.insert(None, Node(125)), True)
        self.assertEqual(s_list.find(125).value, 125)


    def test_insert_empty_list_2(self):
        s_list = LinkedList()
        self.assertEqual(s_list.insert(175, 125), False)

    def tearDown(self):
        pass

