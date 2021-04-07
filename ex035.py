c1 = float(input('Digite o valor da primeira reta '))
c2 = float(input('Digite o valor da segunda reta '))
c3 = float(input('Digie o valor da terceira reta '))
if (c1 < c2+c3) or (c2 < c1+c3) or (c3 < c1+c2):
    print('Pode se formar um triângulo com esses valores')
else:
    print('Infelizmente esse número não pode formar um triângulo')
