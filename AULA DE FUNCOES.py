


def fatorial(num =1):
    x = 1
    for c in range(num, 0, -1):
        x *= c
    return x



for x in range(0, 10):
    b = int(input("u numero int\n"))

    test = fatorial(fatorial(b))

    print('\nR:', test)

