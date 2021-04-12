from datetime import date
dados = dict()
dados["Nome"] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: '))
dados["Idade"] = date.today().year - nascimento
dados["CTPS"] = int(input('Carteira de trabalho (Digite "0" se não tem carteira): '))
if dados["CTPS"] != 0:
    dados["contratação"] = int(input('Ano de contratação: '))
    dados["salário"] = float(input('Salário: R$'))
    dados["aposentadoria"] = (dados["contratação"] + 35) - nascimento
    print('-=' * 30)
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
else:
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')