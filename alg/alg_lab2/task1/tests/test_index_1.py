import psutil
import time
from alg.alg_lab2.task1.src.index_1 import merge_sort
t_start = time.perf_counter()
arr_1=[1,2,3,4,5,6,7,8]
arr_2=[12,45,2,100,67,122,-1,9]
arr_3=[int(i) for i in range(10**9 - 10**4 + 1, 10**9 + 1)][::-1]
print(merge_sort(arr_1))
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


