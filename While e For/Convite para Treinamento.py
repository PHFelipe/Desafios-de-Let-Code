n = int(input())
n1 = int(input())
acm = 0
if n > n1:
    for i in range (n1,n+1):
        if i >= 0:
            acm += i
    print(acm)
else:
    for i in range (n,n1+1):
        if i >= 0:
            acm += i      
    print(acm)