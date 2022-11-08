n = int(input())
if n < 0:
    print("Falso")
else:
    i = 1
    acm = 0
    acm1 = 0
    for i in range(1, n+1):
        calculo = i * (i+1) * (i+2)
        if calculo == n:
            acm = 1
            acmi = i
    
    if acm == 1:
        print(f"{acmi} * {acmi+1} * {acmi+2} = {n}")
        print("Verdadeiro")
    else:
        print("Falso")