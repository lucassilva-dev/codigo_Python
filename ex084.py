pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor}KG. Peso de ', end='')
for x in pessoas:
    if x[1] == menor:
        print(f'{x[0]}', end=' ')







