from random import randint
from time import sleep

while 1:
    numero = int(input('adivinhe o numero que estou pensando de 0 a 5? ').capitalize())
    print('pensando...'.upper())
    sleep(3)
    random = randint(0, 5)
    if numero == random:
        print('você acertou!\n'.capitalize())
    else:
        print(f'Errou! o numero que pensei foi {random}\n')
