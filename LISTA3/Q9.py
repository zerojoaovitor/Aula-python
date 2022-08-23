import random
#lista com os numeros que serão sroteados
lista1 = list(range(0, 9))
lista2 = list(range(0, 9))

#sorteio das cinco dezenas
for c in range(0,5):
    num1 = random.choice(lista1)
    num2 = random.choice(lista2)
    if (num1 == 0) and (num2 == 0):    #caso o numero seja "00" um novo sorteio sera feito
        while (num1 != 0) or (num2 != 0):
            num1 = random.choice(lista1)
            num2 = random.choice(lista2)
    print('dezena sorteada: ',num1,num2)

