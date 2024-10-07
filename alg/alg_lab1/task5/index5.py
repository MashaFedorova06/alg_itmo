import psutil
import time
import random
t_start = time.perf_counter()
def insertion_sort(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(n, arr):
    for i in range(n - 1):
        min_num = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_num]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]
    return arr
  
with open ("input.txt","r") as file:
    n=int(file.readline())
    arr=[int(i) for i in file.readline().split()]
with open("output.txt","w") as file:
    if 0<=n<=10**3 and min(arr)>=-10**9 and max(arr)<10**9:
        #testMaxArr = [random.randint(-10**9, 10**9) for i in range(10**5)]
        #selection_sort(n,testMaxArr) 
        selection_sort(0,[0])
        file.write(" ".join(str(a) for a in arr))
    else:
        print("Число в массиве по модулю превосходит 10^9 или количсетво элементов не соответствует ограничниям")
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")