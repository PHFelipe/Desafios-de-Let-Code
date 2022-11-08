temperatura = float(input())
secrecao = str(input())

if temperatura >= 37 and secrecao == "S" or secrecao == "s":
    print("Exames Especiais")
elif temperatura >= 37 and secrecao == "N" or secrecao == "n":
    print("Exames Basicos")
elif temperatura <= 37 and secrecao == "N" or secrecao == "n":
    print("Liberado")
elif temperatura <= 37 and secrecao == "S" or secrecao == "s":
    print("Exames Basicos")
else:
    print("Erro")