nota1 = float(input('Qual a sua primeira nota ? '))
nota2 = float(input('Qual a sua segunda nota ? '))
media = (nota1+nota2)/2
if media < 5:
    print('Você foi reprovado esta com média abaixo de 5, sua media é {:.1f}'.format(media))
elif media >= 5 and media <= 6.9:
    print('Você esta com recuperação sua media esta entre 5 e 6,9, sua média é {:.1f}'.format(media))
elif media >= 7:
    print('Você foi aprovado, PARABÉNS!!! sua média é {}'.format(media))

6