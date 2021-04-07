soma = 0 #acumulador
contador = 0 #contador
for c in range(0, 7):
    n = int(input('Digite um número inteiro: '))
    if n%2 == 0:
        soma += n #Aqui esta sendo feito o seguinte, se o resto de n divido por 2 for 0 ele vai somar o valor de n com 0 nesse caso se for 7 numeros pares ele vai somar 7 vezes
        contador += 1 #Aqui ta querendo dizer que cada vez que aparecer um número par ele vai contar 1, é um contador verdadeiro
print('A somatória dos {} números pares desses seis números é {}'.format(contador, soma))
