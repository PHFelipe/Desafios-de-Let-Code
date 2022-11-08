origem = int(input())

if origem == 1:
    print("Nordeste")
elif origem == 2:
    print("Norte")
elif origem <= 3 or origem <= 4:
    print("Centro-Oeste")
elif origem <= 5 or origem <= 9:
    print("Sul")
elif origem <= 10 or origem <= 15:
    print("Sudeste")