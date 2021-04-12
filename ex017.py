import math
n1 = float(input('Qual o comprimento do cateto oposto ? : '))
n2 = float(input('Qual o comprimento do cateto adjacente ? '))
total = math.hypot(n1, n2)
print('A hipotenusa entre {} e {} é {:.2f} '.format(n1, n2, total))
