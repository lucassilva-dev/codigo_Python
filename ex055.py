pesomaior = 0
pesomenor = 0
for pessoa in range(1, 6):
    n1 = float(input('Peso da {} pessoa KG:'.format(pessoa)))
    if pessoa == 1:
        pesomaior = n1
        pesomenor = n1
    else:
        if n1 > pesomaior:
            pesomaior = n1
        if n1 < pesomenor:
            pesomenor = n1
print('O maior peso lido foi de {}KG'.format(pesomaior))
print('O menor peso lido foi de {}KG'.format(pesomenor))
