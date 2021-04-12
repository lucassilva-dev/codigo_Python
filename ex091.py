from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
for jogador in range(1, 5):
    sorteio = randint(1, 6)
    print(f'O jogador {jogador} tirou {sorteio} no dado.')
    sleep(1)
    resultados[f"Jogador {jogador}"] = sorteio
ranking = list()
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-=' * 35)
print('Ranking dos Jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)


