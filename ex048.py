contador = 0
s = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        print(c)
        s += c
        contador += 1
print('A soma de todos os {} valores solicitados é {}'.format)
