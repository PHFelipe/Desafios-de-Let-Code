acmh = 0
acmf = 0
acmsal = 0
acmsalh = 0
acmsalhf = 0
for i in range(1,11):
    sal = float(input())
    sexo = input()
    
    if sexo == "m":
        acmh += 1
        acmsalhf += sal
        acmsalh += sal
    elif sexo == "f":
        acmf += 1
        acmsalhf += sal
    if sal > acmsal:
        acmsal += sal
        acmsex = sexo
print(acmh)
print(acmf)
print("%.1f"%(acmsalhf/(acmh+acmf)))
print(acmsex)
print("%.1f"%(acmsalh/acmh))