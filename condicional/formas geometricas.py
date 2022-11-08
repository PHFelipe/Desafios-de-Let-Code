figura = str(input())

if figura == "Q" or figura == 'q':
    lado = float(input())
    
    aquadrado = lado * lado
    print(f'{aquadrado:.2f}')
    pquadrado = lado * 4
    print(f'{pquadrado:.2f}')
elif figura == "R" or figura == 'r':
    largura = float(input())
    altura = float(input())
   
    aretangulo = altura * largura
    print(f'{aretangulo:.2f}')
    pretangulo = 2 * (largura + altura)
    print(f'{pretangulo:.2f}')
elif figura == "C" or figura == 'c':
    raio = float(input())
    
    acirculo = 3.14 * raio ** 2
    print(f'{acirculo:.2f}')
    comcirculo = 2 * 3.14 * raio
    print(f'{comcirculo:.2f}')
else:
    print("Nenhuma figura selecionada")