n = str(input('Digite qual o seu sexo [M/F] ')).strip().upper()[0]
while n != 'M' and n != 'F':
    n = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(n))