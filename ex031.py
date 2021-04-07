v = float(input('Qual a distância da viagem ? KM:'))
if v<=200:
    print('A viagem irá custar R${:.2f}'.format(v*0.50))
else:
    print('A sua viagem tem mais de 200KM nesse caso ela irá custar R${:.2f}'.format(v*0.45))
