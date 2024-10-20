import unittest
from alg.alg_lab2.task6.src.index_6 import  find_maximum_subarray
class CaesarTestCase(unittest.TestCase):
    def test_one(self):
        dates = []
        prices = []
        with open("test_input1.txt", 'r') as file:
            name_firm = file.readline()
            while (line := file.readline()) != "":
                arr_file = line.split(" ")
                print(arr_file)
                date = arr_file[0]
                price_str = arr_file[1]
                price = int(price_str)
                dates.append(date)
                prices.append(price)
        profit, buy_date, sell_date = find_maximum_subarray(prices)
        res = [profit, buy_date, sell_date]
        self.assertEqual(res, [46,0,18])

    def test_two(self):
        dates = []
        prices = []
        with open("test_input2.txt", 'r') as file:
            name_firm = file.readline()
            while (line := file.readline()) != "":
                arr_file = line.split(" ")
                print(arr_file)
                date = arr_file[0]
                price_str = arr_file[1]
                price = int(price_str)
                dates.append(date)
                prices.append(price)
        profit,buy_date, sell_date= find_maximum_subarray(prices)
        res = [profit,buy_date, sell_date]
        self.assertEqual(res, [56,8,18])
    def test_three(self):
        dates = []
        prices = []
        with open("test_input3.txt", 'r') as file:
            name_firm = file.readline()
            while (line := file.readline()) != "":
                arr_file = line.split(" ")
                print(arr_file)
                date = arr_file[0]
                price_str = arr_file[1]
                price = int(price_str)
                dates.append(date)
                prices.append(price)
        profit, buy_date, sell_date = find_maximum_subarray(prices)
        res = [profit, buy_date, sell_date]
        self.assertEqual(res, [14,5,13])

