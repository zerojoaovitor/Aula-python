L = []
#L.append(1)
print(L)
a = 'o'
b = 0

for a in L:
    if b != 'o':
        b = input("insira um numero\n")
        L.append(b)
    else:
        print("fim")

print(L)
