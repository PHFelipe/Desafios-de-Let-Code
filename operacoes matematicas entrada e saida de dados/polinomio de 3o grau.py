#Faça um programa que, dados os coeficientes de um
#polinômio de 3o. grau, resolva o polinômio para qualquer
#valor de x dado.

#A leitura dos coeficientes vai do de maior grau para o de menor.

coeficiente1 = int(input())
coeficiente2 = int(input())
coeficiente3 = int(input())
coeficiente4 = int(input())
x = int(input())

print(coeficiente1 * x ** 3 + coeficiente2 * x ** 2 + (coeficiente3 * x) + coeficiente4)