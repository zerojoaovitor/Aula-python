carros = []
consumo = []
gasto = []
custo = 5.50
j =0
i = 0
n = 10
while i != n:
    x = input('Informe o carro\nR:')
    y = float(input('informe o consumo do carro Km/L\nR:'))
    z = custo / y
    carros.append(x)        # recebendo nome dos carros
    consumo.append(y)       # recebendo consumo km/L
    gasto.append(z)         # custo de cada carro para percorrer um km
    i += 1

while j != n:
    if j < 9:
        if consumo[j - 1] > consumo[j]:
            menor_cus = consumo[j]  # valor com o menor consumo
            carro_menor = carros[j]  # carro com o menor consumo

    j += 1

print(f'Modelo de carro mais economico:\n{carro_menor} com {menor_cus}R$/L ') #imprime os carros e seus respecivos consumos
k =0
while k != n:
    print(f'o {carros[k]} tem consumo de {consumo[k]}\n')
    k += 1






