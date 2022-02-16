from random import randint
from time import sleep

print('''\033[0:35mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')

opcao = int(input('Qual é a sua jogada? '))

comp = randint(0, 2)
comp_type = ''
player_type = ''
vencedor = ''

if comp == 0:
    comp_type = 'Pedra'
elif comp == 1:
    comp_type = 'Papel'
elif comp == 2:
    comp_type = 'Tesoura'

if opcao == 0:
    player_type = 'Pedra'
elif opcao == 1:
    player_type = 'Papel'
elif opcao == 2:
    player_type = 'Tesoura'

sleep(1)
print('\033[1:34mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
sleep(1)

if comp == 0 and opcao == 1 or comp == 1 and opcao == 2 or comp == 2 and opcao == 0:
    vencedor = '\033[1:32mJogador VENCE\033[m'
elif comp == opcao:
    vencedor = '\033[1:33mEmpate\033[m'
else:
    vencedor = '\033[1:31mComputador VENCE\033[m'

print('\033[1:33m' + 11 * '-=' + '\033[m')
print('''\033[1:31mComputador\033[m jogou {}
\033[1:32mJogador\033[m jogou {}'''.format(comp_type, player_type))
print('\033[1:33m' + 11 * '-=' + '\033[m')
print(vencedor)
