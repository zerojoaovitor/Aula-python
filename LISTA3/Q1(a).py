#questão 1


pratos = ['','','','','']
i = 0
x = 1
while i < 5:
    if i == 0:
        print('Quis seus 5 pratos preferidos')

    pratos[i] = input(f'{x}° Prato\n')
    i = i + 1
    x = x + 1
print('Seus pratos preferidos são:\n')
for b in pratos:
    print(f'{b}')


