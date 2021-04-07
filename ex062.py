#NÃO CONSEGUI ESSA PORRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#NÃO CONSIGO VEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEY
#NÃO CONSEGUI MANO PORQUE NÃO CONSIGO, PRECISO DE AJUDA

primeiro = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão '))
contador = 1
termo = primeiro
total = 0
mais = 10
print('{} = '.format(primeiro), end='')
while mais != 0:
    total = total + mais
    while contador <= total:
        termo += razao
        contador += 1
        print(primeiro, end='')
        print(' → ' if contador <= 10 else ' = ',end='')
        print('PAUSA')
        mais = int(input('Quantos números você quer mostrar a mais ? '))