somaidade = 0
mediaidade = 0
nomevelho = 0
idadevelho = 0
feminino = 0
idademulher = 0
for pessoa in range(1, 5):
    print('------- {} pessoa -------'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    somaidade += idade
    mediaidade += somaidade / 4
    if pessoa == 1 in 'M':
        nomevelho = nome
        idadevelho = idade
    elif idade > idadevelho in 'M':
        idadevelho = idade
        nomevelho = nome
    if idade < 20 and sexo == 'F':
        idademulher += 1
print('{} mulheres tem menos de 20 anos'.format(idademulher))
print('A média de idade do grupo é de {:.0f} anos'.format(mediaidade))
print('O nome do homem mais velho é {}, ele tem {} anos'.format(nomevelho, idadevelho))




