palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p: #para cada letra na palavra p
        if letra.lower() in 'aeiou': #se a letra estiver em p
            print(letra, end=' ')

