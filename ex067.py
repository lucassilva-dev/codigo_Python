print('='*80)
print('VAMOS FAZER A TABUADA DE UM NÚMERO')
print('SE VOCÊ PEDIR UM NÚMERO NEGATIVO O PROGRAMA SE ENCERRA EX: -2 ')
print('='*80)
valor = 0
contador = 0
while True:
    valor = int(input('Digite um número: '))
    if valor < 0:
        break
    for c in range(0, 11):
        print(f'{valor} x {c} = {valor*c}')
print('TABUADA ENCERRADA COM SUCESSO.VOLTE SEMPRE !!!')