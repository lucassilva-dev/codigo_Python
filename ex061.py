pt = int(input('Digite o primeiro termo '))
razao = int(input('Digite o segundo termo '))
contador = 1
print(pt, end=' → ')
while contador <= 10:
    contador += 1
    pt += razao
    print(pt, end='')
    print(' → ' if contador <= 10 else ' FIM ', end='')




