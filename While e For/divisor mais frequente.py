x = int(input())
div = 0
freqdiv = 0
acmdiv = 0

for i in range(2, x+1):
    n = x
    while n % i == 0:
        n = n // i
        acmdiv += 1
    if acmdiv > freqdiv:
        freqdiv = acmdiv
        div = i
    acmdiv = 0
print(f"mostFrequent: {div}, frequency: {freqdiv}")