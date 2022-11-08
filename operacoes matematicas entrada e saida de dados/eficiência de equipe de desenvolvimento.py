#Escreva um programa que leia a quantidade de linhas
#de um programa (QUANTL), o número de funções existente
#nele (QUANTF), o tamanho da equipe (TAMEQ) e o número
#de bugs (NUMB) encontrados e calcule a eficiência da
#equipe de acordo com a seguinte
#formula: EFICIENCIA = (QUANTL / QUANTF) / TAMEQ – 4.2 x NUMB
#Utilize uma casa decimal de aproximação.

quantl = int(input())
quantf = int(input())
tameq = int(input())
numb = int(input())

efiencia = (quantl/quantf) / tameq - 4.2 * numb
print(f'{efiencia : .1f}')