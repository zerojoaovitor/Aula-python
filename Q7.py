n = int(input("Verificar numeros primos ate:\n"))

if (n > 0) and (n <201):
    lista = list(range(1, n))

m = 0
for x in lista:
    num = x
    for y in lista:
        numero = num % y
        if numero == 0:
            m += 1
    if m == 2:
        print(f'{x} e primo')
    m = 0


