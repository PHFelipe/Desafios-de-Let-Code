n = 0
tp = ""
acm = 0
for i in range(1,8):
    n = int(input())
    tp = str(input())
    if tp == "G" or  tp == "g":
        acm = acm + 16 * n
    elif tp == "P" or tp == "p":
        acm = acm + 10 * n

print(acm)
print((acm//7) * 2)
