#Faça um programa que receba as características
#(massa e altura) de uma pessoa e retorne seu
#IMC - Índice de Massa Corporal.

#O valor de saída deve ser arredondado usando 2 casas decimais.

massa = float(input())
altura = float(input())

print(f'{massa/(altura ** 2):.2f}')