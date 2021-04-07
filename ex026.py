frase = str(input('Digite uma frase qualquer:')).strip().upper()
print('Na sua frase aparece a letra "A" {} vezes'.format(frase.count('A')))
print('A primeira posição do A aparece em {}'.format(frase.find('A')))
print('A última posição do A aparece em {}'.format(frase.rfind('A')))
