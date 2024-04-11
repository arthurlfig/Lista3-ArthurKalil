lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
frequente = 0
maior = 0 
for i in lista:
    contagem = lista.count(i)
    if contagem > maior:
        contagem = maior 
        frequente = i 
print(frequente)
