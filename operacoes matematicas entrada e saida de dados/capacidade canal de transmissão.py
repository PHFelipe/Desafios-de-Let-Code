#Escreva um programa que calcule a quantidade máxima de dados a ser transmitida
# por um usuário levando em consideração a taxa de transmissão maxima de
# vídeo, áudio e dados e a capacidade do canal contratado:

#QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade

#O valor de saída deve ser arredondado usando 2 casas decimais.


Tvideo = float(input())
Taudio = float(input())
Tdados = float(input())
capacidade = float(input())

qdmax = (Tvideo * 5.2 + Taudio * 3.4 + Tdados * 1.5)/capacidade
print(f'{qdmax : .2f}')