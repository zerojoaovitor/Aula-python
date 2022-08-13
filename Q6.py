# questão 6
#LISTA RECEBISDAS PELO USUARIO
list1 = []
list2 = []

#NUMERO DE ELEMENTOS DENTRO DA LISTA
n = 15

#RECEBENDO VALORE PARA AS DUAS LISTA UMA DE CADA VEZ
for i in range(0, n):
    x = list1.append(input('insira uma informação\nR:'))

for j in range(0, n):
    x = list2.append(input('insira uma informação para a outra lista\nR:'))

#EXIBINDO PARA O USUARIO
print('lista 1', list1)
print('lista 2', list2)

#LISTA INTERPOLADA E VARIAVEIS AUXILIARES
list3 = []
rep = 0
rep0 = 0
rep1 = 0


#INTERPOLANDO LISTA
while rep != (n*2):
    x = float(rep % 2)
    if x == 0:
        adc = list1[rep0]
        list3.append(adc)
        rep0 += 1
    else:
        adc = list2[rep1]
        list3.append(adc)
        rep1 += 1
    rep += 1

#PRINTANDO LISTA COM A INTERPOLAÇÃO DAS DUAS LISTAS JA EXISTENTES
print('lista 3', list3)


