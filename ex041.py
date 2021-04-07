from datetime import date
ano = int(input('Qual o ano em que você nasceu? '))
dataatual = date.today()
idade = dataatual.year-ano
if idade <= 9:
    print('Você tem {} anos, está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, está na categoria JUNIOR'.format(idade))
elif idade <= 20:
    print('Você tem {} anos, está na categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos, está na categoria MASTER a maior categoria'.format(idade))
