valor = int(input('digite um valor de 1 a 10: \n'))
if valor > 10:
   valor = int(input('numero ivalido, digite novamente: '))
elif valor < 1: 
    valor = int(input('numero ivalido, digite novamente: '))
for i in range(1,11):
    print(f'{valor} . {i}  = \n {valor * i}')
