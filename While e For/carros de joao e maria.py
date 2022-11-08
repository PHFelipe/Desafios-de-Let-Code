continua = str(input())
if continua.lower() == "n":
    print("zero")
else:
    acmvelo = 0
    maiorvelo = 0
    maiorano = 0
    acmvm = 0
    while True:
        if continua.lower() == "s":
            ano = int(input())
            velo = float(input())
            acmvelo += velo
            acmvm += 1
            if velo >= maiorvelo:
                maiorvelo = velo
            if ano >= maiorano:
                maiorano = ano
        else:
            break
        continua = str(input())
    velomed = acmvelo / acmvm
    print("%.2f"%maiorvelo)
    print(maiorano)
    print("%.2f"%velomed)