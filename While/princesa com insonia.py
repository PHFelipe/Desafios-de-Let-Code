k = int(input())
i = int(input())
m = int(input())
n = int(input())
d = int(input())


agressao = 0
while d > 0:
    if (d % k) == 0 or (d % i) == 0 or (d % m) == 0 or (d % n) == 0:
        agressao += 1
    d -= 1
print(agressao)