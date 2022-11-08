pregos = 1
soma = 0
while True:
    n = int(input())
    resto = n % 2
    if resto == 0:
        soma += n
    else:
        break
pregos += soma // 12
print("%.2f"% (pregos * 7.89))
print((pregos * 12)- soma)