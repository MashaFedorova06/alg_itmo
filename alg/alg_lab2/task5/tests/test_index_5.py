import unittest
from alg.alg_lab2.task5.src.index_5 import majority_element


arr_search=[8,5,10,-1,100]
class CaesarTestCase(unittest.TestCase):
    def test_one(self):
        str_number="1 3 1 2 1 1"
        arr=[int(i) for i in str_number.split()]
        res= majority_element(arr)
        self.assertEqual(res, 1)

    def test_two(self):
        str_number = "0 0 0 0 0"
        arr = [int(i) for i in str_number.split()]
        res = majority_element(arr)
        self.assertEqual(res, 1)
    def test_three(self):
        str_number = "1 2 3 4 5 6"
        arr = [int(i) for i in str_number.split()]
        res = majority_element(arr)
        self.assertEqual(res, 0)

