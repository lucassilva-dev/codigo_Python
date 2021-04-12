emprestimo = float(input('Qual o valor da casa que você esta comprando ? R$'))
salario = float(input('Quanto você recebe por mês ? R$'))
anos = int(input('E quantos anos de financiamento ? '))
c = emprestimo / (anos * 12)
porcento = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(emprestimo, anos), end=' ')
print('A prestação é de R${:.2f}'.format(c))
if c <= porcento:
    print('O empréstimo pode ser concedido')
else:
    print('Você não foi aprovado porque o valor a se pagar é maior que 30% do seu salário')