import unittest

array = [1,2,4,5,7,8,15,18,21,24,25,29,31,33,35,37,39,41,42,43,44,45,50]

def binary_search(arr, value):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return True
        elif array[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return False

class ls24_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_binary_search(self):
        self.assertEqual(binary_search(array, 43), True)
        self.assertEqual(binary_search(array, 2), True)
        self.assertEqual(binary_search(array, 36), False)

    def tearDown(self):
        pass

unittest.main()

