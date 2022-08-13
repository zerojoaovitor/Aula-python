#Questão 4
#tuplas são imutaveis n e possivel adcinoar valores ou tiralos ou seja
#precisamos criar uma lista para receber os valore e depois
#transformalos em uma tupla com o comando "tuple"

valores = ['', '', '', '', '', '', '', '', '', '']
c = int(0)
#receber valores
print('insira um valo entre 1 e 10')
for i in valores:# limitando valores entre 0 e 10
    entrada = int(input("valor:\n"))
    if (entrada >= 1) and (entrada <= 10):
       valores[c] = entrada
       c += 1
    else:
        print('valor fora dos parametros')

#criando uma tupla com os valores de uma lista
valores_tupla = tuple(valores)

#encontrando repetições
print('o nume 5 foi encontrado vezes:', valores_tupla.count(5))

# verificar se o numero e impar ou par
impar = []
par = []

for j in valores_tupla:
    f = j
    resto = float(f % 2)
    if resto != 0:
        impar.append(j)
    else:
        par.append(j)

print(f'numeros impares dentro da tupla {impar}\n')
print(f'numeros pares dentro da tupla {par}\n')

#localizando um numero
print('o 3 foi encontrado nas posições:')
aux = valores_tupla.index(3)
for a in valores_tupla:
    if aux <= 10:
        print(f'posição:{aux}')
        x = aux + 1
        if x <= 10:
            aux = valores_tupla.index(3, x, 10)
















