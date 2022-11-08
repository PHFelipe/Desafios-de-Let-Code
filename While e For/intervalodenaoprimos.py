n = int(input())
i = 1
print(1, end =" ")
while i <= n:
    multiplo2 = i % 2
    multiplo3 = i % 3
    multiplo5 = i % 5
    multiplo7 = i % 7
    #verificacao de nao primos e nao primos primarios
    if multiplo2 == 0 or multiplo3 == 0 or multiplo5 == 0 or multiplo7 == 0:
        #excluo os primos que são 'primarios'
        if i == 2 or i == 3 or i == 5 or i == 7:
            i += 1
        #se nao for um primo primario, ele imprime
        else:
            print(i, end =" ")
            i += 1
    else:
        i += 1