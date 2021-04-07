# Escolhi essa linguagem porque é a que mais tenho conhecimento no momento.
macazona = dict()
apples = []
macazinha = list()

laranjona = dict()
oranges = []
laranjinhas = list()


while True:
    x = int(input('São quantas maçãs ? '))
    for c in range(1, x+1):
        y = int(input(f'Em qual posição a maçã {c} caiu ? '))
        apples.append(y)
    break
while True:
    x = int(input('São quantas laranjas ? '))
    for c in range(1, x+1):
        y = int(input(f'Em qual posição a laranja {c} caiu? '))
        oranges.append(y)
    break

macazona["Apples"] = apples
macazinha.append(macazona.copy())
macazona.clear()
laranjona["Oranges"] = oranges
laranjinhas.append(laranjona.copy())
laranjona.clear()
print(macazinha)
print(laranjinhas)

for x, v in enumerate(macazinha):
    macazinha = v + 4
print(macazinha)

