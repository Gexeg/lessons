import unittest

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None



class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.ascending = True

    def reverse_list(self):
        """ метод для разворота списка"""
        node = self.head
        while node != None:
            temp_node = node.next
            node.next = node.prev
            node.prev = temp_node
            node = node.prev
        temp_tail = self.tail
        self.tail = self.head
        self.head = temp_tail
        if self.ascending:
            self.ascending = False
        else:
            self.ascending = True
        return

    def compare_values(self, value1, value2):
        """ Метод проверяет первое значение больше или равно второго"""
        return value1 >= value2


    def add_in_list(self, num):
        """ Вставка значения в зависимости от сортировки листа"""
        node_for_add = Node(num)
        node = self.head
        if self.head is None:
            self.head = node_for_add
            node_for_add.prev = None
            node_for_add.next = None
            self.tail = node_for_add
            return
        else:
            if self.ascending:
                if self.compare_values(num, self.tail.value):
                    node_for_add.next = None
                    node_for_add.prev = self.tail
                    self.tail.next = node_for_add
                    self.tail = node_for_add
                    return
                elif self.compare_values(self.head.value, num):
                    self.head.prev = node_for_add
                    node_for_add.next = self.head
                    self.head = node_for_add
                    node_for_add.prev = None
                    return
                else:
                    while node != None:
                        if self.compare_values(node.value, num):
                            node_for_add.prev = node.prev
                            node_for_add.next = node
                            node.prev.next = node_for_add
                            node.prev = node_for_add
                            return
                        node = node.next
            else:
                if self.compare_values(self.tail.value, num):
                    node_for_add.next = None
                    node_for_add.prev = self.tail
                    self.tail.next = node_for_add
                    self.tail = node_for_add
                    return
                elif self.compare_values(num,self.head.value):
                    self.head.prev = node_for_add
                    node_for_add.next = self.head
                    self.head = node_for_add
                    node_for_add.prev = None
                    return
                else:
                    while node != None:
                        if self.compare_values(num, node.value):
                            node_for_add.prev = node.prev
                            node_for_add.next = node
                            node.prev.next = node_for_add
                            node.prev = node_for_add
                            return
                        node = node.next

    def find_and_del(self, val):
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

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, value):
        """Метод поиска прерывается в случае нахождения значения, большего чем искомое"""
        node = self.head

        if self.ascending:
            if value > self.tail.value:
                print('Max value in list %s' % self.tail.value)
                return None
            else:
                while node != None:
                    if  value < node.value:
                        return None
                    if value == node.value:
                        return node
                    node = node.next
        else:
            if value < self.tail.value:
                print('Min value in list %s' % self.tail.value)
                return None
            else:
                while node != None:
                    if value > node.value:
                        return None
                    if value == node.value:
                        return node
                    node = node.next

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght


class ListForString(OrderedList):

    def compare_values(self, value1, value2):
        """ сравнение строк """
        return len(value1.strip()) >= len(value2.strip())

list2 = OrderedList()
list2.add_in_list(123)
list2.add_in_list(123)
list2.add_in_list(586)
list2.add_in_list(8937)
list2.add_in_list(400)
list2.add_in_list(8937)


list3 = ListForString()
list3.add_in_list('Hey,')
list3.add_in_list('mister')
list3.add_in_list('!')

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_in_list(self):
        list2.add_in_list(124)
        self.assertEqual(list2.find(124).value, 124)

    def test_add_in_str_list(self):
        list3.add_in_list('blah')
        self.assertEqual(list3.find('blah').value, 'blah')

    def tearDown(self):
        pass

unittest.main()
