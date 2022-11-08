#Faça um programa que calcula o volume de uma esfera a
#partir de um valor de raio (entre 1.0 e 50.0) fornecido
#pelo usuário. Use pi = 3.14. O valor de saída deve ser arredondado
#usando 2 casas decimais.

raio = float(input())
pi = 3.14
calculo = (4 * pi * raio ** 3) / 3
print(f'{calculo:.2f}')
