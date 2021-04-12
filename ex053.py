frase = str(input('Digite uma frase: ')).strip().upper()
s = frase.split()
juntar = ''.join(s)
print(juntar)
inverso = ''
for c in range(len(juntar) - 1, -1, -1):
    inverso += juntar[c]
if inverso == juntar:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')