from random import choice
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
usuario = int(input(''' Vamos lá
 [ 0 ] pedra
 [ 1 ] papel
 [ 2 ] tesoura
 Qual opção você joga ? '''))
print('JO'), sleep(0.6)
print('KEN'), sleep(0.6)
print('PO!!!'), sleep(0.6)
print('-='*11)
if usuario == 0 and computador == 'tesoura':
    print('Usúario jogou pedra e computador jogou {}'.format('tesoura'))
    print('Jogador vence')
elif usuario == 0 and computador == 'papel':
    print('Usuário jogou pedra e computador jogou {}'.format('papel'))
    print('Computador vence')
elif usuario == 0 and computador == 'pedra':
    print('Usuário jogou pedra e computador jogou {}'.format('pedra'))
    print('Deu empate, joguem novamente')
elif usuario == 1 and computador == 'tesoura':
    print('Usuário jogou papel e computador jogou {}'.format('tesoura'))
    print('Computador vence')
elif usuario == 1 and computador == 'papel':
    print('Usuário jogou papel e computador jogou {}'.format('papel'))
    print('Deu empate, joguem novamente')
elif usuario == 1 and computador == 'pedra':
    print('Usuário jogou papel e computador jogou {}'.format('pedra'))
    print('Jogador vence')
elif usuario == 2 and computador == 'tesoura':
    print('Usuário jogou tesoura e computador jogou {}'.format('tesoura'))
    print('Deu empate, joguem novamente')
elif usuario == 2 and computador == 'papel':
    print('Usuário jogou tesoura e computador jogou {}'.format('papel'))
    print('Jogador vence')
elif usuario == 2 and computador == 'pedra':
    print('Usuário jogou tesoura e computador jogou {}'.format('pedra'))
    print('Computador vence')
else:
    print('Opção incorreta, reinicie e tente novamente.')
print('-='*11)