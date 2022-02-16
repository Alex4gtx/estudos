try: # tentar um codigo
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except (ValueError, TypeError): # excessão se um erro de tipo ou erro de valor
    print('Tivemos um problema com os dados que você digitou.') # mostrar erro personalizado
except ZeroDivisionError: # excessão se um erro for de divisão por zero
    print('não é possivel dividir um numero por 0!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
except Exception as erro: # se as anteriores nao for vdd, excessão = erro
    print(f'O erro encontrado foi {erro.__cause__}') # variavel erro foi usado para mostrar o tipo de erro
else: # senão
    print(f'O resultado é {r:.1f}') # mostra o resto da programação
finally: # finalmente / é executado o código abaixo com ou sem erro
    print('volte sempre! obrigado!')
