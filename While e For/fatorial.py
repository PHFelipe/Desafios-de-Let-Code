n = int(input())
acm = 1

while n >= 0:
    for i in range(n,0,-1):
        acm *= i
    print(acm)
    acm = 1
    n = int(input())
   