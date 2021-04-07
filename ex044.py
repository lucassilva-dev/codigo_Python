precoproduto = float(input('Digite o valor do produto a se pagar R$'))
pagamento = int(input('''Digite 1 para pagamento em cheque ou dinheiro
digite 2 para pagamento a vista no cartão 
digite 3 para pagamento em até 2x no cartão 
digite 4 para pagamento em até 3x ou mais no cartão
 qual opção ? '''))
if pagamento == 1:
    print('Você vai ganhar 10% de desconto, o total a se pagar é R${:.2f}'.format(precoproduto - (precoproduto * 10 / 100)))
elif pagamento == 2:
    print('Você vai ganhar 5% de desconto pagando no cartão, o valor a se pagar é R${:.2f}'.format(precoproduto - (precoproduto * 5 / 100)))
elif pagamento == 3:
    print('parcelando em 2 vezes no cartão não tem taxa de juros, você vai pagar R${:.2f} por mês'.format(precoproduto / 2))
elif pagamento == 4:
    print('Parcelando em 3 vezes ou mais no cartão você tera mais 20% de juros no valor total, valor a se pagar R${:.2f}'.format(precoproduto + (precoproduto * 20 / 100)))
