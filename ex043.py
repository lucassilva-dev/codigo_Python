peso = float(input('Qual é o seu peso? KG: '))
altura = float(input('Qual a sua altura? M: '))
imc = peso / (altura**2)
if imc < 18.5:
    print(' IMC Abaixo de 18,5.Você esta com imc abaixo do seu peso seu imc é {:.1f}'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('IMC entre 18,5 e 25.Você esta no peso ideal o imc do seu corpo é {:.1f}'.format(imc))
elif imc >= 25 and imc <= 30:
    print('IMC entre 25 e 30.Você esta sobrepeso, o IMC do seu corpo é {:.1f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('IMC entre 30 e 40.Você esta obeso, o IMC do seu corpo é {:.1f}'.format(imc))
elif imc >= 40:
    print('IMC de 40 ou mais! Você esta com obesidade mórbida, o IMC do seu corpo é {:.1f}, cuide-se.'.format(imc))

