num = int(input('digite um numero inteiro e positivo, para ver seus divisores: \n'))

if num < 0:
    print('numero invalido... ')
    num = int(input('digite novamente'))
for i in range(1, num):
    if num % i == 0:
        print(f'os divisores do {num} são {i}')