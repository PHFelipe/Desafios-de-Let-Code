#Faça um programa que leia um valor representando o gasto
#realizado por um cliente do restaurante COMABEM e imprima
#o valor total a ser pago, considerando os 10% do garçom.


comanda = float(input())
garcom = comanda * 0.1
conta = comanda + garcom

print(f'{conta : .2f}')