print('=' * 40)
print('{:^40}'.format('LOJA DO LUCÃO'))
print('=' * 40)
total = mil = nome = menor = 0
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        mil += 1
    if menor == 0:
        menor = preco
        nome = produto
    elif preco < menor:
        menor = preco
        nome = produto
    continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produto custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')



