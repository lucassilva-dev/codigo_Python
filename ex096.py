print('Controle de terremoto')
print('-' * 20)
def area(l, c):
  a = l * c
  print(f'A área de um terreno {l} x {c} é de {a}m')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)