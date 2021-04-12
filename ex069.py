total = homem = mulher = 0
print('='*35)
print('VAMOS CADASTRAR UMA PESSOA')
print('='*35)
while True:
    idade = int(input('Qual a sua idade ? '))
    sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
    continuar = str(input('Você quer continuar ? [S/N] ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Você quer continuar ? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        total += 1
    if sexo == 'M':
        homem += 1
    if idade <= 20 and sexo == 'F':
        mulher += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total}.')
print(f'Ao todo temos {homem} homem/homens cadastrado(s).')
print(f'E temos {mulher} mulher/mulheres com menos de 20 anos.')
