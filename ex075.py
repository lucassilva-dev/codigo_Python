n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
print(f'O valor 3 apareceu na {n.index(3)+1} posição')

print(f'Os valores pares foram digitados foram ', end='')
for numero in n:
    if n % 2 == 0:
        print(n, end=' ')

