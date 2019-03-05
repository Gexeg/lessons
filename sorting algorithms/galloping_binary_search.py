import unittest

def galloping_binary_search(array, value):
    if len(array) > 0:
        current_index = 0
        end_index = len(array) - 1
        while True:
            if array[current_index] == value:
                return True
            if array[current_index] < value:
                if current_index == 0:
                    current_index = 1
                else:
                    current_index = current_index * 2

                if current_index > end_index:
                    if array[end_index] < value:
                        return False
                    elif array[end_index] == value:
                        return True
                    else:
                        return galloping_binary_search(array[current_index // 2:end_index], value)

            if array[current_index] > value:
                return galloping_binary_search(array[current_index // 2:current_index], value)
    else:
        return False


class ls24_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_galloping_search(self):
        array = [i + 1 for i in range(10)]
        self.assertEqual(galloping_binary_search(array, 4), True)
        self.assertEqual(galloping_binary_search(array, 9), True)

    def test_binary_search_out_of_array(self):
        array = [i + 1 for i in range(10)]
        self.assertEqual(galloping_binary_search(array, 62), False)

    def test_galloping_search_end_of_array(self):
        array = [i + 1 for i in range(10)]
        self.assertEqual(galloping_binary_search(array, 1), True)
        self.assertEqual(galloping_binary_search(array, 10), True)

    def test_galloping_search_null(self):
        array = [i + 1 for i in range(10)]
        self.assertEqual(galloping_binary_search(array, 0), False)

    def tearDown(self):
        pass


