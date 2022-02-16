while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*30)
    for n in range(1, 11):
        print(f'{num} x {n} = {num*n}')
    print('-' * 30)
