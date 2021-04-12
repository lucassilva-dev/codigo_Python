from datetime import date
ano = date.today()
maioridade = 0
menoridade = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em qual ano você nasceu? '))
    if ano.year - nascimento >= 18:
        maioridade += 1
    elif ano.year - nascimento < 18:
        menoridade += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maioridade))
print('E também tivemos {} pessoas menores de idade'.format(menoridade))