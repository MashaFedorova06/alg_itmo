strInput=input()
a,b=map(int,strInput.split())
while not(-10**9<=a<=10**9 and -10**9<=b<=10**9):
   print("Числа неверны, введите ещё раз ")
   a,b=map(int,strInput.split())
print(a+b**2)

