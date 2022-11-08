n = 0
acm = 0
kg = 0
while kg < 18:
    n = int(input())
    kg += n
    if kg <= 18:
        acm += 1
print(acm)