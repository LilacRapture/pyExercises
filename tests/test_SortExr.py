from src.sortExr import *

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

class TestUtilityFunctions(unittest.TestCase):

    def test_parses_to_int(self):
        is_int = is_parses_to_int("3")
        not_int = is_parses_to_int("dzfgz")
        self.assertTrue(is_int)
        self.assertFalse(not_int)

    def test_get_sort_algorithm(self):
        self.assertEqual(get_sort_algorithm("bubble"), bubble_sort, "not found")
        self.assertIsNone(get_sort_algorithm("kjhnk"))

if __name__ == '__main__':
    unittest.main()
