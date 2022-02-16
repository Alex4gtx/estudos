from random import randint

com = randint(0,10)
print('sou seu computador...\nacabei de pensar em um numero entre 0 e 10\nserá que você consegue adivinhar qual foi?')
tentativas = 0
resp = 11
while resp != com:
    resp = int(input('qual é o seu palpite? '))
    if resp > com:
        print('menos... tente mais uma vez.')
        tentativas += 1
    elif resp < com:
        print('mais... tente mais uma vez')
        tentativas += 1
print('acertou com {} tentativas, parabens!'.format(tentativas))
