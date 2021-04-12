lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
for c, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
