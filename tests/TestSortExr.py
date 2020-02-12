from src.sortExr import insert_sort, choice_sort, bubble_sort

import unittest

# Simple test
class TestSortMethods(unittest.TestCase):

    # expected value
    sorted_list_of_ints = [1, 2, 3, 4, 5]

    def setUp(self):
        self.list_of_ints = [4, 2, 5, 1, 3]

    def test_insert_sort(self):
        insert_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

    def test_choice_sort(self):
        choice_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

    def test_bubble_sort(self):
        bubble_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

# Test for list with repetitive values
class TestSortMethodsRepetitive(unittest.TestCase):

    # expected value
    sorted_list_of_ints = [1, 2, 2, 4, 4]

    def setUp(self):
        self.list_of_ints = [4, 2, 4, 2, 1]

    def test_insert_sort(self):
        insert_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

    def test_choice_sort(self):
        choice_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

    def test_bubble_sort(self):
        bubble_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

# Test for generated list
class TestSortMethodsGenerated(unittest.TestCase):

    # expected value
    sorted_list_of_ints = list(range(20))

    def setUp(self):
        self.list_of_ints = list(range(10, 20)) + list(range(0, 10))

    def test_insert_sort(self):
        insert_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

    def test_choice_sort(self):
        choice_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

    def test_bubble_sort(self):
        bubble_sort(self.list_of_ints)
        self.assertEqual(self.list_of_ints, self.sorted_list_of_ints, "not sorted")

    if __name__ == '__main__':
        unittest.main()
