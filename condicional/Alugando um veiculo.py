diaria = int(input())
km = int(input())

limite = diaria * 90
extra = km - diaria * 100

if extra <= 0:
    print(f'{limite:.2f}')
elif extra > 0:
    print(f'{extra * 12 + limite:.2f}')