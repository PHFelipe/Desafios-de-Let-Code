salario = float(input())
rendacomp= float(input())
 
limite = (salario * 0.3) - rendacomp

if limite >= 0 :
    print(f'{limite:.2f}')
else:
    print("0.00")