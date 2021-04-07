import random
a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do Quarto aluno? ' ))
nomes = [a1, a2, a3, a4]
random.shuffle(nomes)
print('A ordem de apresentação é {} '.format(nomes))




