solucao = float(input())

while solucao != -1:
    if solucao < 7:
        print("ACIDA")
    if solucao > 7:
        print("BASICA")
    if solucao == 7:
        print("NEUTRA") 
    solucao = float(input())