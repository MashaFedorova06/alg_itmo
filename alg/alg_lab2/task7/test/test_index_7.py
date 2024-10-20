import psutil
import time
import random
from alg.alg_lab2.task7.src.index_7 import max_subarray
t_start = time.perf_counter()
arr_1=[ 1,2,3,4,5]
arr_2=[12,-45,2,100,67,122]
arr_4=[4, 5, 3, -2, 9, -2]
arr_3=[random.randint(-10**9, 10**9) for _ in range(10**4)]
print(max_subarray(arr_4))
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")