#Calcule o comprimento do arco de uma circunferência
#(a curva AB na figura) e a área do seu setor
#(delimitado pelo arco e hachurado de cinza na figura)
#usando os seguintes parâmetros:

#O raio da circunferência (entre 1.0 e 50.0)
#A medida do ângulo em graus (entre 0.0 e 359.0)
#Use pi = 3.14
#O valor de saída deve ser arredondado usando 2 casas decimais.

raio = float(input())
alfa = float(input())

comprimento = 2 * 3.14 * raio * (alfa / 360)
area = (3.14 * (raio ** 2) * alfa) / 360

print("%.2f" % comprimento,"%.2f" % area, sep="\n")