T1 = int(input())
T2 = int(input())
T3 = int(input())
T4 = int(input())

if T1 >= 2 and T1 <= 6 and T2 >= 2 and T2 <= 6 and T3 >= 2 and T3 <= 6 and T4 >= 2 and T4 <= 6:
    print((T1 - 1) + (T2 - 1) + (T3 - 1) + T4)
else:
    print("Requisito violado")