n = int(input('Digite um número inteiro qualquer e vamos mostrar a sua tabuada: '))
print('=-'*20)
for c in range(1, 11):
    print(n, 'x', c, '= {}'.format(n*c))
print('=-'*20)