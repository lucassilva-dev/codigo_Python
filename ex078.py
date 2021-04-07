valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(input(f'Digite um valor para a posição {c} '))
print('-=' * 35)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)}, na(s) posição/posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)}, na(s) posição/posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
