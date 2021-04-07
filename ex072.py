numero = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
usuario = int(input('Digite um número entre 0 e 20: '))
while usuario > 20:
    usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numero[usuario]}')
