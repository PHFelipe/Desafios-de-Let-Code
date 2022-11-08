n = input().split()
ni = int(n[0])
nf = int(n[1])
anosbi = 0 
while ni <= nf:
    multiplo4 = ni % 4
    multiplo100 = ni % 100
    multiplo400 = ni % 400
    if multiplo4 == 0 or multiplo400 == 0:
        if multiplo100 == 1:
            ni += 1
        else:
            print(ni)
            ni += 1
            anosbi +=1
    else:
        ni += 1
if anosbi == 0:
    print("-1")