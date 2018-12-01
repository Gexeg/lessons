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


class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_find(self):
        list2 = LinkedList2()
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(124))
        list2.add_in_tail(Node(8937))
        self.assertEqual(list2.find(124), list2.head.next)
        self.assertEqual(list2.find(124).value, 124)

    def test_find_none(self):
        list2 = LinkedList2()
        self.assertEqual(list2.find(124), None)

    def test_find_all(self):
        list2 = LinkedList2()
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(124))
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(12))
        self.assertEqual(len(list2.find_all(12)), 5)

    def test_delete_node_single_node(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(175))
        s_list.delete(175)
        self.assertEqual(s_list.find(175), None)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_delete_node_from_head(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(155))
        s_list.delete(175)
        self.assertEqual(s_list.find(175), None)

    def test_delete_node_from_tail(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(175))
        s_list.delete(175)
        self.assertEqual(s_list.find(175), None)

    def test_delete_node_from_empty_list(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.delete(175), False)

    def test_delete_all_nodes(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(175))
        s_list.delete(175, True)
        self.assertEqual(s_list.find(175), None)

    def test_delete_all_nodes_2(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(175))
        s_list.delete(175, True)
        self.assertEqual(s_list.find(175), None)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_delete_all_nodes_3(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(175))
        s_list.delete(175, True)
        self.assertEqual(s_list.find(175), None)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_delete_all_nodes_4(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(125))
        s_list.delete(175, True)
        self.assertEqual(s_list.find(175), None)
        self.assertEqual(s_list.head.value, 125)
        self.assertEqual(s_list.tail.value, 125)

    def test_insert_empty_list(self):
        s_list = LinkedList2()
        s_list.insert(None, Node(175))
        self.assertEqual(s_list.find(175).value, 175)
        self.assertEqual(s_list.head.value, 175)
        self.assertEqual(s_list.tail.value, 175)

    def test_insert_empty_list_2(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.insert(175, 125), False)

    def test_insert_in_tail_afternode_None(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(155))
        s_list.insert(None, Node(175))
        self.assertEqual(s_list.find(175).value, 175)
        self.assertEqual(s_list.tail.value, 175)

    def test_insert_in_tail_has_afternode(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(165))
        s_list.insert(165, Node(175))
        self.assertEqual(s_list.find(175).value, 175)
        self.assertEqual(s_list.tail.value, 175)

    def test_clean(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(175))
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(175))
        s_list.clean()
        self.assertEqual(s_list.find(175), None)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_add_in_head(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(155))
        s_list.add_in_tail(Node(155))
        s_list.add_in_head(Node(175))
        self.assertEqual(s_list.find(175).value, 175)
        self.assertEqual(s_list.head.value, 175)

    def test_add_in_head_empty_list(self):
        s_list = LinkedList2()
        s_list.add_in_head(Node(175))
        self.assertEqual(s_list.find(175).value, 175)
        self.assertEqual(s_list.head.value, 175)
        self.assertEqual(s_list.tail.value, 175)

    def tearDown(self):
        pass
