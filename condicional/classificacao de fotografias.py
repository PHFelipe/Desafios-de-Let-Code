psnr = int(input())
enquadramento = str(input())
exposicao = str(input())

psnrbom = psnr >= 80 and psnr <= 90
enquadbomexc = enquadramento == "bom" or enquadramento == "excelente"
expoextremo = exposicao == "subexposta" or exposicao == "superexposta"

psnrbaixo = psnr >= 50 and psnr <= 80
enquadtop = enquadramento == "excelente"
exposta = exposicao == "bem exposta"

psnrlixo = psnr < 50 
enquadlixo = enquadramento == "excelente"
expolixo = exposicao == "bem exposta"

if psnrbom and enquadbomexc and exposicao == "bem exposta":
    print("para imprimir")
elif psnrbom and enquadbomexc and expoextremo:
    print("boa")
elif psnrbom:
    if enquadramento != enquadbomexc and exposicao != expoextremo:
        print("marromeno")
elif psnrbaixo and enquadtop and exposta:
    print("boa")
elif psnrbaixo: 
    if enquadramento != enquadtop and exposicao != exposta:
        print("marromeno")
elif psnrlixo and enquadlixo and expolixo:
    print("marromeno")
elif psnrlixo:
    if enquadramento != enquadlixo and exposicao != expolixo:
        print("lixo")