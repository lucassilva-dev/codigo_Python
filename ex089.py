alunos = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = nota1 + nota2 / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 50)
print(f'{"No.":<4}{"NOME:":<10}{"MÉDIA:":>8}')
print('-' * 40)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 40)
while True:
    aluno = int(input('Mostrar notas de qual aluno? ["999" para interromper]'))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno <= len(alunos) - 1:
        print(f'Notas de {alunos[aluno][0]} são {alunos[aluno][1]}')
print('<<< VOLTE SEMPRE >>>')

