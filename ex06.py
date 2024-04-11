cont = 0 
while cont != 10:
    numeros = int(input('digite 10 numeros:\n'))
    cont += 1 

    if numeros >= 10 and numeros <=20:
        print('esse numero faz parte do intervalo entre 10 e 20')
    else:
        print('esse numero não faz parte do intervalo ente 10 e 20')