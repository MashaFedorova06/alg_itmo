import time
t_start = time.perf_counter()
with open("input2.txt","r") as file:
   n= int(file.readline())
   file.close()
if (n < 0 or n > 45 ):
    print("Неправильное введённое число!")
else:
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    with open("output2.txt","w") as file:
        file.write(str(a))
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))

