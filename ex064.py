numero = contador = total = 0
numero = int(input('Digite um número [ se digitar "999" o programa para ]: '))
while numero != 999:
    total += numero
    contador += 1
    numero = int(input('Digite um número [ se digitar "999" o programa para ]: '))
    if numero == 999:
        print('Você digitou {} números e a soma entre eles é {}'.format(contador, total))

