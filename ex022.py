nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome em maiúsculo fica assim {}'.format(nome.upper()))
print('Seu nome em minúsculo fica assim {}'.format(nome.lower()))
print('Seu nome tem no total {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))


