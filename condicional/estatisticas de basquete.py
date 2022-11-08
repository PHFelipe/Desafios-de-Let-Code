time = str(input())
if time != "GSW" and time != "HOU" and time != "CLE" and time != "BOS":
    print("Nenhum time de interesse jogando.")
else:
    nome = str(input())
    arremessotent2 = int(input())
    arremessoconv2 = int(input())
    arremessotent3 = int(input())
    arremessoconv3 = int(input())

    pontostotais = arremessoconv2 + (0.5 * arremessoconv3)/ (arremessotent2+arremessotent3)
    parremess2pts = arremessoconv2 / arremessotent2
    parremess3pts = arremessoconv3 / arremessotent3
    indobem2pts = parremess2pts >= 0.5 and arremessotent2 >= 10
    indobem3pts = parremess3pts >= 0.4 and arremessotent3 >= 7
    lenda = parremess2pts == 1 or parremess3pts == 1
    
    if pontostotais >= 30 or indobem2pts or indobem3pts or lenda:
        print("O time", time,"estah jogando, e", nome,"estah indo bem.")
    else: 
        print("O time", time,"estah jogando, mas", nome,"nao estah indo bem.")