peso,acm = 0,0
for i in range(1,8):
    peso = float(input())
    acm += peso
    if peso >= 560:
        break
print(i)
print("%.1f"%acm)