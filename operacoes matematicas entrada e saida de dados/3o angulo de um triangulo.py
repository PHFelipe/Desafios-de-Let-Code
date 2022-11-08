#Escreva um programa em C que o usuário entre com dois
#ângulos internos de um triângulo e o programa calcule
#o 3o ângulo do triângulo.


angulo1 = float(input())
angulo2 = float(input())
angulo3 = 180 - (angulo1 + angulo2)
print("3o angulo="f'{angulo3 :.6f}')