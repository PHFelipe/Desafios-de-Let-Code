#Calcule a velocidade média das moléculas de um gás a partir dos
#seguintes parâmetros:

#Temperatura do gás em Kelvin (0.0 até 200.0)
#A massa molar do gás (1.0 até 200.0)
#A constante universal dos gases perfeitos (8.31)
#O valor de saída deve ser arredondado usando 2 casas decimais.

#Pesquise como fazer a operação de raiz quadrada.


import math

Temperatura = float(input())
Massa = float(input())
constante = 8.31

calculo = (3 * constante * Temperatura) / Massa
raiz = math.sqrt(calculo)

print(f'{raiz :.2f}')