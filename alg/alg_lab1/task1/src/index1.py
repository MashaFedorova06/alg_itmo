import psutil
import time
import random
t_start = time.perf_counter()
with open ("input.txt","r") as file:
    n=int(file.readline())
    arr=[int(i) for i in file.readline().split()]
def insertionSort(n,arr):
    if n <= 1:
        return 
    for i in range(1, n):  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
with open("output.txt","w") as file:
    if 0<=n<=10**3 and min(arr)>=-10**9 and max(arr)<10**9:
        #testMaxArr = [random.randint(-10**9, 10**9) for i in range(10**3)] 
        insertionSort(n,arr)
        file.write(" ".join(str(a) for a in arr))
    else:
        print("Число в массиве по модулю превосходит 10^9 или количсетво элементов не соответствует ограничниям")
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")