escala = str(input())
temperatura = float(input())

#nessa parte eu poderia colocar todos esses calculos
#apenas no if, no entanto prefiri colocar fora, pois
#facilita a compreensão desse codigo 

kf = 1.8 * (temperatura - 273.15) + 32
fk = (temperatura + 459.67) * (5/9)
kc = temperatura - 273.15
ck = 273.15 + temperatura
fc = (temperatura - 32) / 1.8
cf = (temperatura * 1.8) + 32

if escala == "C" and temperatura >= -273.15:
    #print(f'{cf:.2f} F \n{ck:.2f} K')
    print(f'{cf:.2f} F')
    print(f'{ck:.2f} K')
elif escala == "F" and temperatura >= -459.67:
    #print(f'{fc:.2f} C \n{fk:.2f} K')
    print(f'{fc:.2f} C')
    print(f'{fk:.2f} K')
elif escala == "K" and temperatura >= 0.0:
    #print(f'{kc:.2f} C \n{kf:.2f} F')
    print(f'{kc:.2f} C')
    print(f'{kf:.2f} F')
else:
    print("Valor de temperatura abaixo do minimo")