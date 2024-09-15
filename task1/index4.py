with open ("input.txt","r") as file:
    a,b=map(int,file.readline().split())
with open("outline.txt","w") as file:
    file.write(str(a+b**2))


    