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
        return None

    def find_and_del(self, val):
        """Задание номер 1 метод для поиска и удаления узла по значению"""
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
        """Задание номер 2 метод для поиска и удаления всех узлов по значению"""
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
        """Задание номер 3 метод для очистки списка"""
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
        """Задание номер 4 метод для поиска всех узлов по значению"""
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)
            node = node.next
        return node_list

    def len(self):
        """Задание номер 5 метод для измерения длины списка"""
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def find_and_paste(self, val, node_val):
        """Задание номер 6 метод для помещения узла после заданного узла"""
        node = self.head
        node_for_paste = Node(node_val)
        while node is not None:
            if node.value == val:
                node_for_paste.next = node.next
                node.next = node_for_paste
                return
            node = node.next
        return 'Узел не найден'

s_list = LinkedList()
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(125))

a_list = LinkedList()
a_list.add_in_tail(Node(20))
a_list.add_in_tail(Node(20))
a_list.add_in_tail(Node(20))
a_list.add_in_tail(Node(20))
a_list.add_in_tail(Node(20))

def summ_list_if(list1, list2):
    """Задание номер 7 На входе 2 списка. Если их длины идентичны, то функция возвращает список, каждый элемент которого равен сумме элементов входных списков"""
    new_list = LinkedList()
    if list1.len() == list2.len():
        node_1 = list1.head
        node_2 = list2.head
        while node_1 is not None:
            new_node = Node(node_1.value + node_2.value)
            new_list.add_in_tail(new_node)
            node_1 = node_1.next
            node_2 = node_2.next
        return new_list
    else:
        new_list.add_in_tail(Node('Что-то тут не так'))
        return new_list



# Тест для первого задания
s_list.find_and_del(55)
if s_list.find(55) is None:
    print('Узел удален')

s_list.add_in_tail(Node(55))

s_list.print_all_nodes()
print()

# Тест для второго задания
s_list.find_all_and_del(12)
if s_list.find(12) is None:
    print('Узлы удалены')

s_list.print_all_nodes()
print()

# Тест для третьего задания
s_list.clean()
if s_list.head is None and s_list.tail is None:
    print('List clean')

s_list = LinkedList()
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(128))

# Тест для 4 задания
if len(s_list.find_all(12)) == 2:
    print('4 Working')

# Тест для 5 задания
if s_list.len() == 4:
    print('5 Working')

# Тест для 6 задания
s_list.find_and_paste(55, 125)
if s_list.find(125) is not None:
    print('6 Working')

s_list.print_all_nodes()
print()

# Тест для 7 задания
sum_list = summ_list_if(s_list, a_list)
if sum_list.len() == 5 and sum_list.find(145) is not None:
    print('7 Working')
