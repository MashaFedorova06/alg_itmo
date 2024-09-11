import time
t_start = time.perf_counter()
with open("input2.txt","r") as file:
   n= int(file.readline())
file.close()
if (n < 0 and n > 45 ):
    print("Неправильное введённое число!")
else:
    def calc_fib(n):
        if (n <= 1):
            return n
        return calc_fib(n - 1) + calc_fib( n - 2 )
    with open("output2.txt","w") as file:
        file.write(str(calc_fib(n)))
    file.close()
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))

