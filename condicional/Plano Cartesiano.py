x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("Primeiro Quadrante") 
elif x < 0 and y > 0:
    print("Segundo Quadrante")
elif x < 0 and y < 0:
    print("Terceiro Quadrante")
elif x > 0 and y < 0:
    print("Quarto Quadrante")
elif x == 0 and y == 0:
    print("Sobre a origem")
elif x == 0 and y > 0 or y < 0:
    print("Sobre o eixo y")
elif y == 0 and x > 0 or x < 0:
    print("Sobre o eixo x")