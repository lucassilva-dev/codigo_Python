print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
precos = ('Lápis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90)
for pos in range(0, len(precos)):
    if pos % 2 == 0:
        print(f'{precos[pos]:.<30}', end='')
    if pos % 2 != 0:
        print(f'R${precos[pos]:>7.2f}')
