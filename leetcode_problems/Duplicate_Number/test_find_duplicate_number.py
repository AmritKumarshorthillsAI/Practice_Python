import unittest
import find_duplicate_number

class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate(self):
        self.assertEqual(find_duplicate_number.find_duplicate([1,3,4,2,2]), 2)
        self.assertEqual(find_duplicate_number.find_duplicate([3,1,3,4,2]), 3)
        self.assertEqual(find_duplicate_number.find_duplicate([1,1]), 1)
        self.assertEqual(find_duplicate_number.find_duplicate([1,2,2,3,4,5]), 2)
        self.assertEqual(find_duplicate_number.find_duplicate([2,2,2,2,2]), 2)

if __name__ == "__main__":
    unittest.main()
