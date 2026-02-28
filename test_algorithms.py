import unittest
from algorithms import bubble_sort, binary_search

class TestAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        # Normal case
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        # Empty list
        self.assertEqual(bubble_sort([]), [])
        # Single element
        self.assertEqual(bubble_sort([1]), [1])
        # Already sorted
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        # Reverse sorted
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])
        # Negative numbers
        self.assertEqual(bubble_sort([-1, -3, 5, 0]), [-3, -1, 0, 5])

    def test_binary_search(self):
        # Normal cases
        arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(binary_search(arr, 25), 3)
        self.assertEqual(binary_search(arr, 11), 0)
        self.assertEqual(binary_search(arr, 90), 6)
        # Element not found
        self.assertEqual(binary_search(arr, 100), -1)
        self.assertEqual(binary_search(arr, -5), -1)
        # Empty array
        self.assertEqual(binary_search([], 1), -1)
        # Single element array
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1], 2), -1)

if __name__ == '__main__':
    unittest.main()
