matriz = [[], [], []]
par = soma = maior = 0
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 30)
print(f'[  {matriz[0][0]:^4}  ][  {matriz[0][1]:^4}  ][  {matriz[0][2]:^4}  ]')
print(f'[  {matriz[1][0]:^4}  ][  {matriz[1][1]:^4}  ][  {matriz[1][2]:^4}  ]')
print(f'[  {matriz[2][0]:^4}  ][  {matriz[2][1]:^4}  ][  {matriz[2][2]:^4}  ]')
print('-=' * 30)
for cont in matriz[0]:
    if cont % 2 == 0:
        par = cont
for cont in matriz[1]:
    if cont % 2 == 0:
        par += cont
    if maior == 0:
        maior = cont
        if cont > maior:
            maior = cont
for cont in matriz[2]:
    if cont % 2 == 0:
        par += cont
    soma = cont + cont
print(f'A soma de todos os valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

