idade = int(input())
if idade < 18:
    print("Nao pode adotar")
else:
    parente = str(input())
    conjunta = str(input())
    casados = str(input())
    idadeadot = int(input())
    paisdest = str(input())
    consentimentopais = str(input())
    consentimentoadot = str(input())
    
    verifidade = (idade - idadeadot) >= 16 
    v1 = paisdest == "N" and consentimentopais == "S"
    
    if parente == "N" and verifidade and conjunta == "S" and casados == "S":
        if v1: 
            if idadeadot >= 12:
                if consentimentoadot == "S":
                    print("Pode adotar")
                else:
                    print("Nao pode adotar")
            else:
                print("Pode adotar")
        else: 
            print("Nao pode adotar")
    elif parente == "N" and verifidade and conjunta == "N":
        if v1: 
            if idadeadot >= 12:
                if consentimentoadot == "S":
                    print("Pode adotar")
                else:
                    print("Nao pode adotar")
            else:
                print("Pode adotar")
        else: 
            print("Nao pode adotar")
    else:
        print("Nao pode adotar")