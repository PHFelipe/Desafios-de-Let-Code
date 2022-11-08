sem = int(input())
if sem < 0 or sem > 10:
    print("entrada invalida")
else:
    chdisciplina = int(input())
    notdisciplina = int(input())
    situacao = input()

    multi = 0
    somanota = 0 
    cre = 0

    while sem > 0 and sem < 10:
        if situacao != "T" and situacao != "AD" and situacao != "DE" and situacao != "AE" and situacao != "DD" and situacao != "DE":
            if chdisciplina == 33 or chdisciplina == 50 or chdisciplina == 67 or chdisciplina == 83:
                cre = cre + chdisciplina
                multi = notdisciplina * chdisciplina
                somanota = somanota + multi
                
        sem = int(input())
        
        if sem > 0 and sem < 10: 
            chdisciplina = int(input())
            notdisciplina = int(input())
            situacao = input()
            
    if somanota != 0 or multi != 0 or cre != 0:
        crefin = somanota / cre 
        print("%.2f" % crefin)
        

    else:
        print("entrada invalida")