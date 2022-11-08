glicose = int(input())

contglicose = 0
somaglico = 0

while glicose != 0:
    contglicose = contglicose + 1
    somaglico = somaglico + glicose
    
    glicose = int(input())
    mediaglicose = somaglico/contglicose
    
    if glicose == 0:

        if mediaglicose == 0:
            print("Glicose Normal")
        if mediaglicose <= 110:
            print("Glicose Normal")
        elif mediaglicose >= 200:
            print("Glicose Muito Alta")
        else:
            print("Glicose Alterada")
    
    