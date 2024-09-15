import time
t_start = time.perf_counter()
with open("input3.txt","r") as file:
   n = int(file.readline())
with open("ounput3.txt","w") as file:
        if (n <= 1):
            file.whrite(str(n))
        else:
             a,b=0,1
             for i in range(n):
               a,b=b,a+b
             with open("output3.txt","w") as file:
               file.write(str(a%10))
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
