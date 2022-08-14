fixa = {}
doc = []
pessoa_mai_30 = []
pessoa_men_30 = []
n = 10  # numero de pessoas cadastradas

#recebendo informações das pessoas
for c in range(0,n):
    fixa['NOME'] = str(input('Nome: '))
    fixa['IDADE'] = int(input('Idade: '))
    doc.append(fixa.copy())

voltas = 0

#salvando as informações em uma lista

while voltas != n:
    if doc[voltas]['IDADE'] >= 30:
        add_pessoa_30 = doc[voltas]['NOME']
        pessoa_mai_30.append(add_pessoa_30)
    else:
        add_pessoa = doc[voltas]['NOME']
        pessoa_men_30.append(add_pessoa)
    voltas += 1

print('pessoas com menos de 30 anos:\n', pessoa_men_30,'\n\npessoas com mais de 30 anos:\n', pessoa_mai_30)





