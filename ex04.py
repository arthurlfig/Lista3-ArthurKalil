cont = 3 
soma = 0
while cont == 0:
    idade = int(input("digite sua idade: \n"))
    soma += idade
    cont +=1
if cont == 3:
    media = soma/cont  
    print(f'a média das idades é: {media}')