n1 = int(input())
n2 = int(input())

if n1 > n2:
    for i in range(n1 - 1, n2, -1):
        multiplo2 = i % 2
        multiplo3 = i % 3
        multiplo5 = i % 5
        multiplo7 = i % 7

        if multiplo2 != 0 and multiplo3 != 0 and multiplo5 != 0 and multiplo7 != 0:
            print(i)
else:
    for i in range(n2, n1, -1):
        multiplo2 = i % 2
        multiplo3 = i % 3
        multiplo5 = i % 5
        multiplo7 = i % 7

        if multiplo2 != 0 and multiplo3 != 0 and multiplo5 != 0 and multiplo7 != 0:
            print(i)
    if n1 == n2:
        multiplo2 = n1 % 2
        multiplo3 = n1 % 3
        multiplo5 = n1 % 5
        multiplo7 = n1 % 7
        if n1 == 2 or n1 == 3 or n1 == 5 or n1 == 7:
            print(n1)
        elif multiplo2 != 0 and multiplo3 != 0 and multiplo5 != 0 and multiplo7 != 0:
            print(n1) 