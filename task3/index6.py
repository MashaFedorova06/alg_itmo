import time
t_start = time.perf_counter()
with open("input3.txt","r") as file:
   n = int(file.readline())
with open("ounput3.txt","w") as file:
        if (n <= 1):
            file.whrite(str(n))
        else:
             a0=0
             a1=1
             sumNum=0
             for i in range(1,n):
                  sumNum=(a0+a1)%10
                  a0=a1
                  a1=sumNum
             file.write(str(sumNum))
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
