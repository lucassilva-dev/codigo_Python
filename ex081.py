lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')



