crimedelator = str(input())
if crimedelator != "roubo" and crimedelator != "tráfico" and crimedelator != "homicídio":
    print("Crime inválido.")
else:
#solicitaçao do crime do delator e verificaçao de existencia do crime 
    if crimedelator == "homicídio":
        crimedelatado = str(input())
        if crimedelator != "roubo" and crimedelator != "tráfico" and crimedelator != "homicídio":
            print("Crime inválido.")    
#homicídio delatando homicídio         
        if crimedelatado == "homicídio":
            print("Delação concedida.")
#homicídio delatando roubo ou tráfico
        if crimedelatado == "roubo" or crimedelatado == "tráfico":
            print("Delação rejeitada.")
    else:
#solicitaçao de entradas e verificaçao se o crime é valido        
        valor = int(input())
        crimedelatado = str(input())
        if crimedelatado != "roubo" and crimedelatado != "tráfico" and crimedelatado != "homicídio":
            print("Crime inválido.")
        else:    
            if crimedelator == "tráfico" or crimedelator == "roubo":
                if crimedelatado == "homicídio":
                    print("Delação concedida.")
#crimes que necessitam ser pesados
                else:       
                    if crimedelator == "roubo" and crimedelatado == "roubo":
                        valordelatado = int(input())  
                        cincovezes = valordelatado / 5
                        if valor < cincovezes:
                            print("Delação concedida.")
                        else: 
                            print("Delação rejeitada.")
#---------------------------------------------------------------    
                    elif crimedelator == "roubo" and crimedelatado == "tráfico":
                        valordelatado = int(input())  
                        trezvezes = valordelatado / 3
                        if valor < trezvezes:
                            print("Delação concedida.")
                        else:
                            print("Delação rejeitada.")
#--------------------------------------------------------------- 
                    elif crimedelator == "tráfico" and crimedelatado == "tráfico":
                        valordelatado = int(input())  
                        cincovezes = valordelatado / 5
                        if valor < cincovezes:
                            print("Delação concedida.")
                        else:
                            print("Delação rejeitada.")
#---------------------------------------------------------------       