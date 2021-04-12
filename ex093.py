jogador = dict()
gols = list()
total = 0
jogador["Nome"] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
for c in range(1, partidas + 1):
    golos = (int(input(f'Quantos gols na partida {c} ')))
    gols.append(golos)
    total += golos
jogador["Gols"] = gols[:]
jogador["Total"] = total[:]
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i in range(0, len(jogador["Gols"])):
    print(f'{"=>":>4} Na partida {i}, fez {jogador["Gols"][i]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')






