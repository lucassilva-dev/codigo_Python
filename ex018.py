import math
n1 = float(input('Digite o valor de um ângulo qualquer '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print(' O ângulo {} tem como seno {} como cosseno {} e como tangente {}'.format(n1, sen, cos, tan))
