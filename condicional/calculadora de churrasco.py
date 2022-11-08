tpcarne = str(input())
if tpcarne != "C" and tpcarne != "BF" and tpcarne != "BS":
    print("Opção inválida.")
else:
    palho = str(input())
    bebidasadult = str(input())
    bebidascrian = str(input())
    qtdcrian = int(input())
    qtdadult = int(input())

    churrascoc = ((0.2 * qtdadult) * 32) +((0.2 * qtdcrian) * 32)+ ((0.1 * qtdadult) * 18) + ((0.1 * qtdadult)* 15)  
    churrascobf = ((0.25 * 32)* qtdadult) + ((0.2 * 32)* qtdcrian) + ((0.15 * 18)* qtdadult) 
    churrascobs = ((0.25 * 32)* qtdadult) + ((0.2 * 32)* qtdcrian) + ((0.15 * 15)* qtdadult)
    bebidapcrian = (6 * (0.5 * qtdcrian))
    bebidapadult = (8 * (2 * qtdadult))
   
    if palho == "N":
        #bebida pra criança e para adulto
        if tpcarne == "C" and bebidasadult == "S" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+bebidapadult+churrascoc - bebidapcrian+bebidapadult+churrascoc:.2f}')
        elif tpcarne == "BF" and bebidasadult == "S" and bebidascrian == "S":
            print("R$:",f'{bebidapcrian+bebidapadult+churrascobf-((bebidapcrian+bebidapadult+churrascobf)* 0.02):.2f}')
        elif tpcarne == "BS" and bebidasadult == "S" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+bebidapadult+churrascobs -((bebidapcrian+bebidapadult+churrascobs)* 0.02):.2f}')
        #bebida apenas para criança
        elif tpcarne == "C" and bebidasadult == "N" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+churrascoc -((bebidapcrian+churrascoc)* 0.02):.2f}')
        elif tpcarne == "BF" and bebidasadult == "N" and bebidascrian == "S":
            print("R$:",f'{bebidapcrian+churrascobf -((bebidapcrian+churrascobf)* 0.02):.2f}')
        elif tpcarne == "BS" and bebidasadult == "N" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+churrascobs -((bebidapcrian+churrascobs)* 0.02):.2f}')
        #bebida apenas para adulto
        elif tpcarne == "C" and bebidasadult == "S" and bebidascrian == "N":
            print("R$:", f'{bebidapcrian+churrascoc-((bebidapcrian+churrascoc)* 0.02):.2f}')
        elif tpcarne == "BF" and bebidasadult == "S" and bebidascrian == "N":
            print("R$:",f'{bebidapcrian+churrascobf-((bebidapcrian+churrascobf)* 0.02):.2f}')
        elif tpcarne == "BS" and bebidasadult == "S" and bebidascrian == "N":
            print("R$:", f'{bebidapcrian+churrascobs-((bebidapcrian+churrascobs)* 0.02):.2f}')
    else:
    #acima codigo com desconto, abaixo codigo sem desconto
    #bebida pra criança e para adulto
        if tpcarne == "C" and bebidasadult == "S" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+bebidapadult+churrascoc:.2f}')
        elif tpcarne == "BF" and bebidasadult == "S" and bebidascrian == "S":
            print("R$:",f'{bebidapcrian+bebidapadult+churrascobf:.2f}')
        elif tpcarne == "BS" and bebidasadult == "S" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+bebidapadult+churrascobs:.2f}')
        #bebida apenas para criança
        elif tpcarne == "C" and bebidasadult == "N" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+churrascoc:.2f}')
        elif tpcarne == "BF" and bebidasadult == "N" and bebidascrian == "S":
            print("R$:",f'{bebidapcrian+churrascobf:.2f}')
        elif tpcarne == "BS" and bebidasadult == "N" and bebidascrian == "S":
            print("R$:", f'{bebidapcrian+churrascobs:.2f}')
        #bebida apenas para adulto
        elif tpcarne == "C" and bebidasadult == "S" and bebidascrian == "N":
            print("R$:", f'{bebidapcrian+churrascoc:.2f}')
        elif tpcarne == "BF" and bebidasadult == "S" and bebidascrian == "N":
            print("R$:",f'{bebidapcrian+churrascobf:.2f}')
        elif tpcarne == "BS" and bebidasadult == "S" and bebidascrian == "N":
            print("R$:", f'{bebidapcrian+churrascobs:.2f}')
        #sem bebida
        elif tpcarne == "BF" and bebidasadult == "N" and bebidascrian == "N":
            print("R$:", f'{churrascobf:.2f}')
        elif tpcarne == "C" and bebidasadult == "N" and bebidascrian == "N":
            print("R$:", f'{churrascoc:.2f}')
        elif tpcarne == "BS" and bebidasadult == "N" and bebidascrian == "N":
            print("R$:", f'{churrascobs:.2f}')