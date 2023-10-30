import unittest

def bin_search(a, key):            # function to search for key element
    l, r = 0, len(a) - 1

    while l <= r:
        mid = (l + r) // 2
        if a[mid] == key:
            return mid              # key found at mid index
        elif a[mid] < key:
            l = mid + 1
        else:
            r = mid - 1

    return -1  # Target element is not present

class TestBinarySearch(unittest.TestCase):                           # test class for containing various test methods

    def test1(self):                                                 # test1 used to check for the target element present in array
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        key = 7
        result = bin_search(numbers, key)
        self.assertEqual(result, 6)

    def test2(self):                                                 # test2 used to check for the target element not present in array
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        key = 11
        result = bin_search(numbers, key)
        self.assertEqual(result, -1)

    def test3(self):                                                 # test3 used to check whether it checks for duplicate target elements or not
        numbers = [19, 23, 2, 1, 47, 47, 59, 59]
        key = 47
        result = bin_search(numbers, key)
        self.assertIn(result, [4, 5])

    def test4(self):                                                  # test4 used to check whether it will work for empty array or not
        numbers = []
        key = 5
        result = bin_search(numbers, key)
        self.assertEqual(result, -1)

    def test5(self):                                                   # test5 used to check whether the program works for non int values
        numbers = [1.0, 2.5, 3.75, 5.25, 6.0]
        key = 6.0
        result = bin_search(numbers, key)
        self.assertEqual(result, 4)
    
    def test6(self):                                                  # test6 used to check whether the program works for large sized arrays or not
        numbers = list(range(150, 50000))
        key = 5486
        result = bin_search(numbers, key)
        self.assertEqual(result, 5336)
    

if __name__ == '__main__':                                             # program initiator
    unittest.main()
