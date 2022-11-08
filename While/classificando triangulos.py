lados = input().split()

while lados[0] != "FIM":
    l1 = int(lados[0])
    l2 = int(lados[1])
    l3 = int(lados[2]) 
    escaleno = l1 != l2 != l3 
    isoceles = l1 == l2 or l2 == l3 or l3 == l1
    triang = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)
    if triang:
        if l1 == l2 == l3:
            print("EQUILATERO")
        elif isoceles:
            print("ISOSCELES") 
        elif escaleno:
            print("ESCALENO")
    else:
        print("INVALIDO")
    lados = input().split()
