from random import randint
computador = randint(0, 10)
contador = 0
imparpar = impar = 0
print('-='*50)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*50)
while True:
    jogador = int(input('Qual o valor? '))
    parimpar = str(input('Par ou ímpar [P/I] ')).strip().upper()[0]
    soma = computador + jogador
    while parimpar not in 'PpIi':
        parimpar = str(input('Par ou ímpar [P/I] ')).strip().upper()[0]
    if soma % 2 == 0:
        imparpar = 'Par'
    elif soma % 2 != 0:
        imparpar = 'Ímpar'
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total foi {soma}, é um número {imparpar}')
    if soma % 2 == 0 and parimpar == 'P':
        print('VOCÊ VENCEU !!!')
        print('VAMOS JOGAR NOVAMENTE.')
        contador += 1
        computador = randint(0, 10)
    elif soma % 2 != 0 and parimpar == 'I':
        print('VOCÊ VENCEU !!!')
        print('VAMOS JOGAR NOVAMENTE.')
        contador += 1
        computador = randint(0, 10)
    elif soma % 2 == 0 and parimpar == 'I':
        break
    elif soma % 2 != 0 and parimpar == 'P':
        break
print('VOCÊ PERDEU !!!')
print('-='*40)
print(f'GAME OVER! Você venceu {contador} vezes/vez')
print('-='*40)
