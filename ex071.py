print('=' * 35)
print('Banco Lucas')
print('=' * 35)
valor = int(input('Qual valor você quer sacar ? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced >= 1:
            print(f'Total de {totalced} cédulas de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 35)
print('Volte sempre ao banco Lucas')
print('=' * 35)