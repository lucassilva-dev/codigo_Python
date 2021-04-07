n = int(input('Digite um numero inteiro '))
contador = 0
contador2 = 0
for c in range(1, n+1):
    if n % c == 0:
        print((c), end=' ')
        contador += 1
    else:
        print((c), end=' ')
print('\n O número {} foi divisível {} vezes'.format(n, contador))
if contador == 2:
    print('Por isso esse número é primo')
else:
    print('Portanto esse número não é primo')
#meu metódo o de cima é do guanabara !

#contador = 0
#n = int(input('Digite um número: '))
#for count in range(1, n+1):
#    print(count, end=' ')
#    if n % count == 0:
#        contador += 1
#if contador == 2:
#    print('''\nO valor {} foi divisível 2 vezes
#PORTANTO ELE É PRIMO'''.format(n))
#else:
#    print('\nO número {} foi divisível {} vezes, por isso ele não é primo'.format(n, contador))