lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
frequente = 0
maior = 0 
for i in range(1,11):
     inst = lista.count(i)
     if inst > maior:
        contagem = maior 
        frequente = i 
print(frequente)
