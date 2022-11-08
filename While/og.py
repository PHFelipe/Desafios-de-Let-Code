filhos = input().split()

while filhos[0] != "0" and filhos[1] != "0":
    f1 = int(filhos[0])
    f2 = int(filhos[1])
    soma = f1 + f2 
    print(soma)
    filhos = input().split()
