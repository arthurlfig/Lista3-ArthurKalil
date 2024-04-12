lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
frequente = 0
maiorFreq = 0
for num in lista:
    if lista.count(num) > frequente:
        maiorFreq = lista.count(num) 
        frequente = num

print(f'{frequente}')