n1 = float(input('Quantos Km esse carro alugado andou ? KM: '))
n2 = int(input('Por quantos dias esse carro foi alugado ? Dias: '))
km = 60*n2
dia = 0.15*n1
total = km + dia
print('Você andou {}Km com esse carro e alugou ele por {} dias'.format(n1, n2))
print('Você vai ter que pagar pelos km rodados R${:.2f} e pelos dias alugado R${:.2f}'.format(km, dia))
print('No total dos dois valores você vai pagar R${:.2f}'.format(total))
