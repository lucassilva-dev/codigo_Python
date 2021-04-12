from time import sleep
def dormida():
    sleep(1.0)


def maior(*num):
    if len(num) > 0:
        print(f'O maior de {num} é o {max(num)}')
    else:
        print('Nennhum valor foi informado.')


maior(20, 30, 140, 50, 60)
dormida()
maior(40, 5, 3, 10)
dormida()
maior(28, 99, 1045, 54654789, 0, 3, 8, 784155)
dormida()
maior(14)
dormida()
maior(1, 8)
dormida()
maior()