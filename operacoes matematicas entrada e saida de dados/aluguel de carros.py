

dias = int(input())
km = int(input())

pdiaria = dias * 30
kmrodado = km * 0.01

total = (pdiaria + kmrodado) - ((pdiaria + kmrodado )* 0.1)

print("%.2f" % total)