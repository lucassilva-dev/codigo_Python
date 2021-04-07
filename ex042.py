c1 = float(input('Digite o valor da primeira reta '))
c2 = float(input('Digite o valor da segunda reta '))
c3 = float(input('Digie o valor da terceira reta '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Pode se formar um triângulo com esses valores', end=' ')
    if c1 == c2 == c3:
        print('Esse triângulo tem todos os lados iguais, ele é equilátero')
    elif c1 != c2 != c3 != c1:
        print('Este triângulo tem todos os lados diferentes, é escaleno')
    else:
        print('Este triângulo tem dois lados iguais, ele é isósceles')
else:
    print('Esses valores não dão para formar um triângulo')