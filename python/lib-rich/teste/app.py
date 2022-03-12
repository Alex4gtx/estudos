import functionspy as fp

moedas = {'dl': 'Dolar Americano', 'btc': 'Bitcoin', 'brl': 'Real'}

# separação

fp.tabelaEscolha(moedas)
print('Escolha a primeira moeda:')
primeiraMoeda = fp.input_valueVerification(moedas)
print('Escolha a segunda moeda:')
segundaMoeda = fp.input_valueVerification(moedas)
