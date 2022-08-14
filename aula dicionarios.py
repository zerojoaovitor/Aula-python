dados = {'nome': 'thais chata',
        'idade':  '45 anos'}


def space():
    print('\n\n----------------------------------------\n\n')


print(dados['nome']) # printa uma elemento dentro de uma categoria

dados['sexo'] = 'F' # adiciona uma nova categoria

print(dados)

#del dados['idade']       apaga uma categoria
space()

print(dados.values())   # imprime o que tem dentro da categoria isso e chamado de VALUES
print(dados.keys())     # imprime as categorias q são chamadas de KEYS
print(dados.items())    # tudo que tem dentro

# exemplo de for com dictionary

space()
for a,b in dados.items():
    print(f'seu {a} e tem {b}')

# como funciona o posicionamento dos dictionerys
space()

#acontece de um dicionario existir dentro de uma lista
teste1 = [{'nome': 'thais chata',       'idade': '45 anos',  'sexo': 'F'},    #posição 0
          {'nome': 'joão super legal',  'idade': '19 anos',  'sexo': 'M'},    #posição 1
          {'nome': 'flavinho do penel', 'idade': '20 anos',  'sexo': 'M'}]    #posição 2

print(teste1[]['nome'])
print(teste1[]['sexo'])


space()



