tabela = 'Atlético MG', 'Internacional', 'Flamengo', 'Palmeiras', 'Sport', 'Santos', 'São Paulo', 'Fluminense', 'Vasco da Gama', 'Fortaleza', 'Grêmio', 'Bahia', 'Corinthians', 'Atletico-GO', 'Athletico-PR', 'Ceará', 'Coritiba', 'Bragantino', 'Botafogo', 'Goiás'
print('-=' * 35)
print(f'''Os primeiros colocados são 
1 - {tabela[0]}
2 - {tabela[1]}
3 - {tabela[2]}
4 - {tabela[3]}
5 - {tabela[4]}''')
print('-=' * 35)
print(f'''Os útltimos 4 colocados da tabela são
1 - {tabela[16]}
2 - {tabela[17]}
3 - {tabela[18]}
4 - {tabela[19]}''')
print('-=' * 35)
print(f'O Santos está em {len(tabela[5])-1}')
print('-=' * 35)
print(f'Os times em ordem alfabética')
print(sorted(tabela))




