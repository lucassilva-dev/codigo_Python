from random import randint
from time import sleep
lista = list()
def sorteio():
    print(f'Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        sleep(0.5)
        print(f'{n}', end=' ')


def soma():
    somaa = 0
    print(f'\nSomando os valores pares de {lista}, ', end='')
    for p in lista:
        if p % 2 == 0:
            somaa += p
    print(f'temos {somaa}')


sorteio()
soma()
print('\nFIM')