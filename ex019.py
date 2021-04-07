import random
aluno1 = str(input('Qual o nome do primeiro aluno? '))
aluno2 = str(input('Qual o nome do segundo aluno? '))
aluno3 = str(input('Qual o nome do terceiro aluno? '))
aluno4 = str(input('Qual o nome do quarto aluno? '))
sorte = (aluno1, aluno2, aluno3, aluno4)
resp = random.choice(sorte)
print('O aluno sorteado que vai apagar o quadro é o(a) {}'.format(resp))

