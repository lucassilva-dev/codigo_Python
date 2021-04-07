vel = float(input('Qual a velocidade que estava o carro? KM:'))
if vel >80:
    print('Você foi multado por excesso de velocidade a multa custará R${:.2f}'.format((vel-80)*7))
else:
    print('Parabéns você não excedeu o limite de velocidade')