#Em uma escola, um professor deve realizar 
#três avaliações por semestre. Para o cálculo
# da nota final, ele pode usar três diferentes 
#métodos de cálculo de médias:

#Média aritmética ("a");

#Média ponderada ("p"): nesse caso, o programa deve perguntar também os pesos de cada nota;

#Média harmônica ("h"): pode ser definida pela quantidade de notas dividida pela soma do inverso
# de cada nota. Ex.: Se as notas forem 10, 7 e 5, a média harmônica será 3/(1/10+1/7+1/5)

#Faça um programa que calcula as três médias para 
#um conjunto de 3 notas. Na saída também deve ser i
#dentificado a qual média cada valor se refere.

nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
peso1 = int(input())
peso2 = int(input())
peso3 = int (input())

maritmetica = (nota1 + nota2 + nota3)/ 3
mponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
mharmonica1 = (1/nota1) + (1/nota2) + (1/nota3) 
mharmonica2 = 3 / mharmonica1

print("a: " "%.1f" % maritmetica, "p: " "%.1f" % mponderada, "h: " "%.1f" % mharmonica2, sep = "\n" )
