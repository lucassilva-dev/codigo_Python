valores = [[], []]
for c in range(1, 8):
    numeros = int(input(f'Digite o {c}o valor: '))
    if numeros % 2 == 0:
        valores[0].append(numeros)
    if numeros % 2 != 0:
        valores[1].append(numeros)
print('-=' * 40)
print(f'Os valores pares digitados foram {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram {sorted(valores[1])}')


