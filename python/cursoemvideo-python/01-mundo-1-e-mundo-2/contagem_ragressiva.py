from time import sleep

print((20*'\033[1:33m-=\033[m')+'\n'+'{: ^40}'.format(' CONTAGEM REGRESSIVA ')+'\n'+(20*'\033[1:33m-=\033[m'))

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print((20*'\033[1:31m-=\033[m')+'\n'+'{: ^40}'.format(' BOOOM!! BOOOM!!! BOOOM! ')+'\n'+(20*'\033[1:31m-=\033[m'))
