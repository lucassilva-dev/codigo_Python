pilha = 0
expr = str(input('Digite a expressão: '))
for cont in expr:
    if cont == '(':
        pilha += 1
    elif cont == ')':
        pilha -= 1
if pilha == 0:
    print('Sua expressão esta correta')
else:
    print('Sua expressão esta errada')


