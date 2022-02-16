distancia = int(input('Digite a distância da sua viagem: '))
print('Você esta prestes a iniciar uma viajem de {}Km.'.format(distancia))

if distancia <= 200:
    distancia = distancia * 0.50
else:
    distancia = distancia * 0.45

print('sua viagem vai custar R${:.2f}'.format(distancia))