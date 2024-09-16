with open ("input.txt","r") as file:
    a,b=map(int,file.readline().split())
file.close()
with open("output.txt","w") as file:
    if -10**9<=a<=10**9 and -10**9<=b<=10**9:
       file.write(str(a+b))
    else:
        print("Числа неверны, введите ещё раз ")
file.close()




   