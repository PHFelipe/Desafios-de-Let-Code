vingador = str(input())
#------------------Verificaçao de vingador--------------------------
if vingador != "Homem de Ferro" and vingador != "Hulk" and vingador != "Capitão América" and vingador != "Thor" and vingador != "Gavião Arqueiro" and vingador != "Viúva Negra":
    print("Vingador Inválido")
else:
    poder = input()
    energia = int(input())

#--------------------Homem de Ferro------------------------
if vingador == "Homem de Ferro" and poder == "Armadura de Ferro" and energia >= 10:
    print("Homem de Ferro conseguiu derrotar Thanos")
elif vingador == "Homem de Ferro" and poder == "Armadura de Ferro" and energia <= 10: 
    print("Homem de Ferro NAO conseguiu derrotar Thanos, chamem outro Vingador")
elif vingador == "Homem de Ferro" and poder == "Escudo":
    print("Homem de Ferro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Capitão América")
elif vingador == "Homem de Ferro" and poder == "Martelo":
    print("Homem de Ferro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Thor")
elif vingador == "Homem de Ferro" and poder == "Força Bruta":
    print("Homem de Ferro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Hulk")
elif vingador == "Homem de Ferro" and poder == "Arco e Flecha":
    print("Homem de Ferro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Gavião Arqueiro")
elif vingador == "Homem de Ferro" and poder == "Inteligência":
    print("Homem de Ferro NAO conseguiu derrotar Thanos")
    print("Esse é o poder da Viúva Negra")
#--------------------Hulk-----------------------------------
if vingador == "Hulk" and poder == "Força Bruta" and energia >= 5:
    print("Hulk conseguiu derrotar Thanos")
elif vingador == "Hulk" and poder == "Força Bruta" and energia <= 5: 
    print("Hulk NAO conseguiu derrotar Thanos, chamem outro Vingador")
elif vingador == "Hulk" and poder == "Escudo":
    print("Hulk NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Capitão América")
elif vingador == "Hulk" and poder == "Martelo":
    print("Hulk NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Thor")
elif vingador == "Hulk" and poder == "Armadura de Ferro":
    print("Hulk NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Homem de Ferro")
elif vingador == "Hulk" and poder == "Arco e Flecha":
    print("Hulk NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Gavião Arqueiro")
elif vingador == "Hulk" and poder == "Inteligência":
    print("Hulk NAO conseguiu derrotar Thanos")
    print("Esse é o poder da Viúva Negra")
#--------------------Capitão América----------------------------
if vingador == "Capitão América" and poder == "Escudo" and energia >= 7:
    print("Capitão América conseguiu derrotar Thanos")
elif vingador == "Capitão América" and poder == "Escudo" and energia <= 7: 
    print("Capitão América NAO conseguiu derrotar Thanos, chamem outro Vingador")
elif vingador == "Capitão América" and poder == "Força Bruta":
    print("Capitão América NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Hulk")
elif vingador == "Capitão América" and poder == "Martelo":
    print("Capitão América NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Thor")
elif vingador == "Capitão América" and poder == "Armadura de Ferro":
    print("Capitão América NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Homem de Ferro")
elif vingador == "Capitão América" and poder == "Arco e Flecha":
    print("Capitão América NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Gavião Arqueiro")
elif vingador == "Capitão América" and poder == "Inteligência":
    print("Capitão América NAO conseguiu derrotar Thanos")
    print("Esse é o poder da Viúva Negra")
#----------------------Thor--------------------------------------
if vingador == "Thor" and poder == "Martelo" and energia >= 4:
    print("Thor conseguiu derrotar Thanos")
elif vingador == "Capitão América" and poder == "Martelo" and energia <= 4: 
    print("Thor NAO conseguiu derrotar Thanos, chamem outro Vingador")
elif vingador == "Thor" and poder == "Força Bruta":
    print("Thor NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Hulk")
elif vingador == "Thor" and poder == "Escudo":
    print("Thor NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Capitão América")
elif vingador == "Thor" and poder == "Armadura de Ferro":
    print("Thor NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Homem de Ferro")
elif vingador == "Thor" and poder == "Arco e Flecha":
    print("Thor NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Gavião Arqueiro")
elif vingador == "Thor" and poder == "Inteligência":
    print("Thor NAO conseguiu derrotar Thanos")
    print("Esse é o poder da Viúva Negra")
#----------------------Gavião Arqueiro-----------------------------
if vingador == "Gavião Arqueiro" and poder == "Arco e Flecha" and energia >= 12:
    print("Gavião Arqueiro conseguiu derrotar Thanos")
elif vingador == "Gavião Arqueiro" and poder == "Arco e Flecha" and energia <= 12: 
    print("Gavião Arqueiro NAO conseguiu derrotar Thanos, chamem outro Vingador")
elif vingador == "Gavião Arqueiro" and poder == "Força Bruta":
    print("Gavião Arqueiro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Hulk")
elif vingador == "Gavião Arqueiro" and poder == "Escudo":
    print("Gavião Arqueiro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Capitão América")
elif vingador == "Gavião Arqueiro" and poder == "Armadura de Ferro":
    print("Gavião Arqueiro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Homem de Ferro")
elif vingador == "Gavião Arqueiro" and poder == "Martelo":
    print("Gavião Arqueiro NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Thor")
elif vingador == "Gavião Arqueiro" and poder == "Inteligência":
    print("Gavião Arqueiro NAO conseguiu derrotar Thanos")
    print("Esse é o poder da Viúva Negra")
#------------------------Viúva Negra-------------------------------
if vingador == "Viúva Negra" and poder == "Inteligência" and energia >= 20:
    print("Viúva Negra conseguiu derrotar Thanos")
elif vingador == "Viúva Negra" and poder == "Inteligência" and energia <= 20: 
    print("Viúva Negra NAO conseguiu derrotar Thanos, chamem outro Vingador")
elif vingador == "Viúva Negra" and poder == "Força Bruta":
    print("Viúva Negra NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Hulk")
elif vingador == "Viúva Negra" and poder == "Escudo":
    print("Viúva Negra NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Capitão América")
elif vingador == "Viúva Negra" and poder == "Armadura de Ferro":
    print("Viúva Negra NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Homem de Ferro")
elif vingador == "Viúva Negra" and poder == "Martelo":
    print("Viúva Negra NAO conseguiu derrotar Thanos")
    print("Esse é o poder do Thor")
elif vingador == "Viúva Negra" and poder == "Arco e Flecha":
    print("Viúva Negra NAO conseguiu derrotar Thanos")
    print("Esse é o poder da Gavião Arqueiro")