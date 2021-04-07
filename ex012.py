n1 = float(input('Qual o preço do produto? R$'))
desconto = (n1*10)/100
total = n1-desconto
print('o preço desse produto de R${:.2f} com 10% de desconto fica R${:.2f}'.format(n1, total))
print('Se você pagar esse produto a vista você tem 10% de desconto!')
p = n1 + (n1*8/100)
print('o preço desse produto de R${:.2f} com o acréscimo de 8% fica R${:.2f}'.format(n1, p))
print('Se você pagar esse produto parcelado você paga com o acréscimo de 8%')
