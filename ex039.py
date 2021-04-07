from datetime import date
sexo = int(input('''Qual o seu sexo?
tecle [1] para masculino
tecle [2] para feminino
opção: '''))
ano = int(input('Qual o seu ano de nascimento? '))
anoatual = date.today()
idade = anoatual.year - ano
if sexo == 1 and idade < 18:
    print('Ainda falta {} ano(s) para você se alistar ao exército'.format(18-idade))
elif sexo == 1 and idade == 18:
    print('Você ja esta na idade para se alistar ')
elif sexo == 2:
    print('Você é do sexo feminino, portanto não precisa se alistar, não é obrigatório no BRASIL')
else:
    print('Você ja passou da idade de se alistar, você atrasou {} ano(s), corra para se alistar'.format(idade-18))
