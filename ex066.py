numero = contador = soma = 0
while True:
    numero = int(input('Digite um número inteiro [999 para o programa parar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print('='*70)
print(f'Foram digitados {contador} número(s) e a soma de todos os valores digitados é {soma}')
print('='*70)