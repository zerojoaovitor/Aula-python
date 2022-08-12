valor_casa = float(input('valor da casa\n'))
salario = float(input('Seu salario\n'))
tempo = float(input('prazo que deseja paga em anos'))

salario_30 = float(salario*0.3)
tempo_mes = tempo*12

#             valor da casa   30% do salario   tempo em mes    prestações por mes
restricoes = [valor_casa,     salario_30,      tempo_mes,      valor_casa/tempo_mes]

if restricoes[3] <= restricoes[1]:
    print(f'seu pediido esta dento das restrições\nsuas prestações:\n{restricoes[3]}')
else restricoes[3] <= restricoes[1]:
    print("seu pedido n esta dentro das restições\n")



