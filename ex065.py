numero = continuar = maior = menor = contador = soma = 0
while continuar != 'n':
    numero = int(input('Digite um número: '))
    continuar = str(input('Você quer continuar ? [s/n] ')).lower().strip()[0]
    soma += numero
    contador += 1
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('Você digitou {} números e a média  foi {}'.format(contador, soma / contador))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
