n = int(input())
acm = 0
andar = 0

while n > 0:
    acm += andar + 1
    if n - acm < 0:
        break
    n -= acm
    andar +=1
print(andar)