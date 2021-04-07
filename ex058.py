from random import randint
sorte = randint(0, 10)
contador = 0
n = int(input('Vamos jogar um joguinho, entre 0 a 10 que número você acha que eu estou pensando? '))
while n != sorte:
    n = int(input('Poxa que pena, não é esse número que estou pensando! Tente outra vez '))
    contador += 1
print('Parabéns você conseguiu eu pensei no número {}'.format(sorte))
print('Você acertou depois de {} tentativas'.format(contador))
