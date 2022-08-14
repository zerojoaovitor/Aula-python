#Crie um programa que exiba uma listagem de preços de produtos em forma tabular.
#Utilize uma tupla única com nomes e preços dos produtos.

lista_precos = ({'PRODUTO': 'Caneta'   , 'VALOR': 1.5},
                {'PRODUTO': 'Borracha' , 'VALOR': 2.5},
                {'PRODUTO': 'Grafite'  , 'VALOR': 3.0},
                {'PRODUTO': 'Lapiseira', 'VALOR': 7.8},
                {'PRODUTO': 'Regua', 'VALOR': 5.0},
                {'PRODUTO': 'Tesoura'  , 'VALOR': 9.5})

i = 0
print('Lista de Preços\t\t\tValor')
print('----------------------------------------')
while i != 6:

    print(lista_precos[i]['PRODUTO'],':\t\t\t\t', lista_precos[i]['VALOR'])
    i += 1

print('----------------------------------------')
