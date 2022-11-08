n = int(input())
if n < 1 or n > 9:
    while n < 1 or n > 9:
        print("Insira um número inicial entre 1 e 9")
        n = int(input())
n1 = int(input())
if n1 < 1 or n1 > 9:
    while n1 < 1 or n1 > 9:
        print("Insira um número final entre 1 e 9")
        n1 = int(input())
if n > n1:
    print("Nenhuma tabuada nesse intervalo")
else:
    for i in range(n,n1+1):
        for j in range(1,10):
            print(f"{i} x {j} = {j*i}")
        if i != n1:
            print("")