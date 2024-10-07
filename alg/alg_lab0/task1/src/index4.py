with open ("input_2.txt","r") as file:
    a,b=map(int,file.readline().split())
with open("output_2.txt","w") as file:
    if -10**9<=a<=10**9 and -10**9<=b<=10**9:
       file.write(str(a+b**2))
    else:
        print("Числа неверны, введите ещё раз ")
    


    