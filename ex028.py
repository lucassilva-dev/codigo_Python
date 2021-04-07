import random
sorte = [0, 1, 2, 3, 4, 5]
resultado = random.choice(sorte)
usuario = int(input('Eu pensei em um número entre 0 a 5.Qual é?  '))
if usuario == resultado:
    print('Você acertou parábens')
else:
    print('Você errou o número correto é {} !'.format(resultado))
