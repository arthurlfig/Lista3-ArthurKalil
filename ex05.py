cont = 0 
while cont != 10:
    numeros = int(input('digite 10 numeros:\n'))
    cont +=1

    if numeros % 2 == 0:
        print('o numero {numeros} é par')
    else:
        print('o numero é impar')