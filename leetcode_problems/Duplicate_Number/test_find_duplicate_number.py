import unittest
import find_duplicate_number

class TestFindDuplicate(unittest.TestCase):
    
    
    def test_find_duplicate_odd_length_list(self):
        self.assertEqual(find_duplicate_number.find_duplicate([1, 2, 3, 4, 5, 3, 6]), 3)

    def test_find_duplicate_even_length_list(self):
        self.assertEqual(find_duplicate_number.find_duplicate([4, 5, 6, 7, 5, 8]), 5)

    def test_find_duplicate_zero_length_list(self):
        with self.assertRaises(ValueError):  # Assuming the function raises an error for an empty list
            find_duplicate_number.find_duplicate([])

    def test_very_long_list(self):
        long_list = [i for i in range(10000)] + [5000]  # Duplicate 5000
        self.assertEqual(find_duplicate_number.find_duplicate(long_list), 5000)

    def test_when_there_is_no_duplicate(self):
        with self.assertRaises(ValueError):  # Assuming the function raises an error when there are no duplicates
            find_duplicate_number.find_duplicate([1, 2, 3, 4, 5])

    def test_when_there_is_one_duplicate(self):
        self.assertEqual(find_duplicate_number.find_duplicate([1, 2, 3, 4, 5, 1]), 1)

    def test_more_than_one_duplicate(self):
        self.assertEqual(find_duplicate_number.find_duplicate([1, 2, 3, 1, 3, 2]), 1)  # First duplicate found

if __name__ == "__main__":
    unittest.main()
