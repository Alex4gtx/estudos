tabela = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino', 'Fluminense',
          'Internacional', 'Ceara-SC', 'America-MG', 'Cuiaba', 'Athletico-PR', 'Santos', 'São Paulo', 'Atletico-GO',
          'Juventude', 'Bahia', 'Gremio', 'Sport Recife', 'Chapecoense')
print(15*'-=')
print('\033[1:32mLista de times do Brasileirão:\033[m ', end='')
for n, times in enumerate(tabela):
    print(times, end='')
    print(', ' if n < 19 else '.', end='')
print('\n'+(15*'-='))
print('\033[1:32mOs 5 primeiros são:\033[m ', end='')
for n, times in enumerate(tabela[:5]):
    print(times, end='')
    print(', ' if n < 19 else '.', end='')
print('\n'+(15*'-='))
print('\033[1:32mOs 4 ultimos são:\033[m ', end='')
for n, times in enumerate(tabela[-4:]):
    print(times, end='')
    print(', ' if n < 19 else '.', end='')
print('\n'+(15*'-='))
print('\033[1:32mTimes em ordem alfabetica:\033[m ', end='')
for n, times in enumerate(sorted(tabela)):
    print(times, end='')
    print(', ' if n < 19 else '.', end='')
print('\n'+(15*'-='))
print(f'\033[1:32mO {tabela[19]} está na {tabela.index("Chapecoense")+1}ª posição.\033[m')
