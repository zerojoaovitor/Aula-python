saida = ['','','','']

x = 0
b = 1
c = 0
while x != 3:

    saida[x] = float(input("Insira sua notas\n"))
    x = x + 1
    b = b + 1
    if x == 3:
        saida[x] = (saida[0] + saida[1] + saida[2])/3
        while b != len(saida):
            if b > 0:
                b = 0
                c = 1
            print(f'indi : {c}')
            print(f'nota: {saida[b]}\n')
            b = b + 1
            c = c + 1

print(f'media {saida[3]}')



