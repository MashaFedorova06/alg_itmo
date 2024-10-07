import psutil
import time
import random

t_start = time.perf_counter()
with open ("input.txt","r") as file:
    n= int(file.readline())
    arr=list(map(int, file.readline().split()))
    
def sort_with_swaps(n,arr):
    swaps=[]
    for i in range(n - 1):
        k = i + 1
        minArr = arr[k]
        for j in range(i + 1, n):
            if arr[j] < minArr:
                minArr = arr[j]
                k = j
        if minArr < arr[i]:
            arr[i], arr[k] = arr[k], arr[i]
            swaps.append([i+1,k+1])
    return swaps
#testMaxArr = [random.randint(-10**9, 10**9) for i in range(10**5)]
#swap_index=sort_with_swaps(n,testMaxArr)       
swap_index = sort_with_swaps(n,arr)
with open('output.txt', 'w') as f:
    if 3<=n<=5000 and min(arr)>=-10**9 and max(arr)<10**9:
       for [x, y] in swap_index:
            f.write(f"Swap elements at indices {x} and {y}.\n")
       f.write("No more swaps needed.")
    else:
        print("Число в массиве по модулю превосходит 10^9 или количсетво элементов не соответствует ограничниям")
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
