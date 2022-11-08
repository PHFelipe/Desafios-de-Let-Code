qtdlivros = int(input())
qtdalunos = int(input())

conceito = qtdalunos / qtdlivros

if conceito <= 8:
    print("A")
elif conceito >= 9 and conceito <= 12: 
    print("B")
elif conceito >= 13 and conceito <=18:
    print("C")
else: 
    print("D")