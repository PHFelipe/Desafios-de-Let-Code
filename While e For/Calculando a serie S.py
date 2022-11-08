n = int(input())
if n == 0:
    print("Sem termos para somar")
else:
    j = 1
    saida = "S= "
    acm = 0
    if n == 0:
        print("Sem termos para somar.")
    else:   
        for i in range(1, n+1):
            if i % 2 != 0:
                acm += j
                saida += f"{j}"
            else:
                acm += j*j/(j*3)
                saida += f"{j*j}/{j*3}"
                j += 1
            if i != n:
                saida += " + "
    print(saida)
    print("%.2f" % acm)