acm = 0
for i in range(1,6):
    print("Digite um valor:")
    n = float(input())
    if n < 0:
        acm += 1
print(f"Foram digitados {acm} numeros negativos")