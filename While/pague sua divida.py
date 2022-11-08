divida = int(input())
pagamento = int(input())

while divida > 0:
    if pagamento >= divida:
        print("(antes)", divida)
        divida = 0
        print("(depois)", divida)
    else:
        print("(antes)", divida)
        divida = divida - pagamento
        print("(depois)", divida)
    