n1 = int(input('Qual o valor do primeiro número ? '))
n2 = int(input('Qual o valor do segundo número ? '))
if n1 > n2:
    print(' o primeiro valor {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print(' o segundo valor {} é maior que {}'.format(n2, n1))
else:
    print('Não existe valor maior, o valor {} e o valor {} são iguais'.format(n1, n2))