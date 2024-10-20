import psutil
import time
from alg.alg_lab2.task3.src.index_3 import count_inversions
t_start = time.perf_counter()
arr_1=[ 1,2,3,4,5]
arr_2=[12,45,2,100,67,122]
arr_3=[int(i) for i in range(10**9 - 10**4 + 1, 10**9 + 1)][::-1]
print( count_inversions(len(arr_3),arr_3))
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
