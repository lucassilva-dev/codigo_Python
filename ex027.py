nome = str(input('Qual o seu nome completo? ')).strip().title()
name = nome.split()
print('O seu primeiro nome é {}'.format(name[0]))
print('O seu útlimo nome é {}'.format(name[-1]))
