senha = ['1', '2', '3', '4']
xs = len(senha)
print(xs)

l = 0
while l != xs:
        escolha = int(input('0 - senha atual\n1 - pegaar senha\n'))
        if escolha == 0:
                print(f'senha atual {senha[xs-1]}')
        elif escolha == 1:
                nova_senha = len(senha) + 1
                senha.append(nova_senha)
                xs = len(senha)
                print(f'senha:{senha[xs-1]}')
        l = l
        print(senha)



