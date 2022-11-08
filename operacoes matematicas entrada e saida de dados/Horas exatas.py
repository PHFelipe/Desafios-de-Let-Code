#Seu Furustreco é um patrão justo. Ele decidiu pagar
#para cada funcionário além de cada hora extra, um
#adicional de 10% sobre cada hora extra.

#Para ajudar seu Furustreco, você deve fazer um programa
#que recebe o salário base do empregado e quantas horas
#extras ele fez naquele mês. Você deve imprimir na saída
#padrão o salário final do empregado.

#Dica: Você deve usar o salário base para calcular quanto
#custa uma hora extra do empregado. Considerando que a carga
#horária mensal de uma pessoa é de 44 horas.

#O valor de saída deve ser arredondado usando 2 casas decimais.

salariob = float(input())
horasextra = int(input())

valorhora = salariob / 44
valoracrescimo = valorhora * horasextra + (valorhora * horasextra * 0.1)

print(f'{salariob+valoracrescimo: .2f}')
