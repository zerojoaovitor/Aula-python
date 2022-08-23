#questão 3

print('responda as questões com::\n 0 - SIM\n 1 - NÃO\n')

#lista com as pergunatas
perguntas = ["Já trabalhou com a vítima?","Devia para a vítima?","Mora perto da vítima?","Esteve no local do crime?","Telefonou para a vítima?"]

#fezendo as perguntas ao usuario e contanto o numero de respostas
r_final = 0
for x in perguntas:
    print(x)
    r1 = int(input())
    if r1 == 1:
        r_final = r_final + 1
    r1 = 0
print('\n\n')

#analisando repostas para para definir conde o entrevistado se enquadra
if r_final == 2:
    print('pessoa suspeita')
elif (r_final >= 3) and (r_final <= 4):
    print('essa pessoa e um cúmplice')
elif r_final == 5:
    print('Ele e o assasino!!!')
else:
    print('não possue envolvimento com o caso')




