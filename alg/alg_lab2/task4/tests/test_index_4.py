import unittest
from alg.alg_lab2.task4.src.index_4 import binary_search
from alg.alg_lab2.task4.src.index_4 import insertionSort

arr_search=[8,5,10,-1,100]
class CaesarTestCase(unittest.TestCase):
    def test_one(self):
        results = []
        for el in arr_search:
            arr_1=[-1,5,3,10,8]
            insertionSort(len(arr_1), arr_1)
            res=binary_search(arr_1, el)
            results.append(str(res))
        str_res = " ".join(results)
        self.assertEqual(str_res, "3 2 4 0 -1")

    def test_two(self):
        results = []
        for el in arr_search:
            arr_2= [6,100,5,0,10]
            insertionSort(len(arr_2), arr_2)
            res = binary_search(arr_2, el)
            results.append(str(res))
        str_res = " ".join(results)
        self.assertEqual(str_res, "-1 1 3 -1 4")
    def test_three(self):
        results = []
        for el in arr_search:
            arr_3 = [0,0,0,0,0]
            insertionSort(len(arr_3), arr_3)
            res = binary_search(arr_3, el)
            results.append(str(res))
        str_res=" ".join(results)
        self.assertEqual(str_res, "-1 -1 -1 -1 -1")

