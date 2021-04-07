salario = float(input('Digite o valor do seu salário R$'))
aumento1 = salario*10/100
aumento2 = salario*15/100
if salario>1250:
    print('Seu salário vai receber um aumento de 10% agora você vai receber R${:.2f}'.format(salario+aumento1))
else:
    print('Seu salário vai receber um aumento de 15% agora você vai receber R${:.2f}'.format(salario+aumento2))
