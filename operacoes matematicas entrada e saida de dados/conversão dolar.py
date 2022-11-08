#Escreva um programa que realize a conversão de dólar
#para real: para cada valor lido em dólar da entrada
#padrão, será exibido o correspondente em reais (1 dólar = 3.55 reais).


real = float(input())
cambio = real * 3.55
print (f'{cambio :.2f}')