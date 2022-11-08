escolha = input()

cinema = 0 
boliche = 0
i = 5

while i >= 0:
    if escolha.lower() == "cinema":
        cinema = cinema + 1
    elif escolha.lower() == "boliche":
        boliche = boliche + 1
    escolha = input()
    i -= 1

if cinema > boliche:
    print("CINEMA")
else: 
    print("BOLICHE")