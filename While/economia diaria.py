dia = float(input())

somadias = 0
somadinheiro = dia
i = 0

while i < 6:
    dia1 = float(input())
    somadinheiro = dia1 + somadinheiro 
    if (dia1 - dia) >= 0.5:
        somadias +=1
    dia = dia1
    i += 1

print("R$", "%.2f" % somadinheiro)
print(somadias)    