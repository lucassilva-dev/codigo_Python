n = int(input('Digite um número que vamos fazer seu fatorial: ')) #N recebe um valor do usuário
c = n #o C vai receber o valor de N
f = 1 #o F vai receber o valor de 1 vai fazer o fatorial
print('5! ') #mostrando o valor 5 "5!" representa fatorial
while c > 0: #enquanto o c for maior que 0
    print('{}'.format(c), end='') #mostre na tela o valor c que é o n digitado pelo usuário, end para naõ pular linha
    print(' X ' if c > 1  else ' = ', end='') #Se c for maior que 1 mostrei X se não mostre igual, end pra não pular linha
    f = f * c #f recebe ele mesmo multiplicado por C
    c -= 1 #c recebe ele mesmo - 1
print(f) #mostre o F

