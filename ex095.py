jogadores = dict()
gols = []
dados = list()
total = 0
while True:
    jogadores.clear()
    nome = str(input('Nome do jogador: ')).strip().title()
    jogadores["Nome"] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols.clear()
    for c in range(1, partidas + 1):
        golss = int(input(f'Quantos gols {nome} fez na partida {c}? '))
        total += golss
        gols.append(golss)
    jogadores["Gols"] = gols[:]
    jogadores["Total"] = total
    dados.append(jogadores.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(dados):
    print(f'{k:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {dados[busca]["Nome"]}:')
        for i, g in enumerate(dados[busca]["Gols"]):
            print(f'     No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')


