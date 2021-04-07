numero = int(input('Qual o valor do número ? '))
print('Entendi, legal você escolheu o número {}'.format(numero))
conversao = int(input('Digite 1 para binário, 2 para octal ou 3 para hexadecimal, qual conversão você quer? '))
if conversao == 1:
    print('Ok o seu número convertido para binário fica {}.'.format(bin(numero)[2:]))
elif conversao == 2:
    print('Ok o seu número convertido para octal fica {}.'.format(oct(numero)[2:]))
elif conversao == 3:
    print('Ok o seu número convertido para hexadecimal fica {}'.format(hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente')
