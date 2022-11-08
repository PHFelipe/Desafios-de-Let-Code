#A diagonal de um polígono é um segmento de linha
#que liga 2 vértices não adjacentes. Faça um programa
#que calcula a quantidade de diagonais de um polígono
#baseado na quantidade de lados desse polígono


lado = int(input())

calculo1 = lado * (lado - 3)
calculo2 = calculo1 / 2

print(f'{calculo2 : .0f}')