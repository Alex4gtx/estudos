vel = int(input('qual a velocidade atual de um carro? ').capitalize())

calculo = 70 + (vel - 80) * 7

if vel > 80:
    print('Você ultrapassou o limite de velocidade! sua velocidade atual é de {}Km/h,'
          ' sua multa será de R${:.2f}.'.format(vel, float(calculo)))
else:
    print(f'Sua velocidade atual de {str(vel)}Km/h está normal!')
