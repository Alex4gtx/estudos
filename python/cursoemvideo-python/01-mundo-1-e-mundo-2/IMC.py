peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura * altura)
message = ''

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    message = 'você está Abaixo do peso normal'
elif imc >= 18.5 and imc < 25:
    message = 'Parabéns, você está na faixa de Peso normal'
elif imc >= 25 and imc < 30:
    message = 'você está acima do peso normal'
elif imc >= 30 and imc < 40:
    message = 'Você está Obeso'
else:
    message = 'Você está em Obesidade mórbida, cuidado!'

print(message)
