def f_text(texto):
    """formata um texto titulo com linhas automaticas"""
    texto = '  '+texto+'  '
    print(f'{len(texto) * "~"}\n{texto.upper()}\n{len(texto) * "~"}')


f_text('alex giovani hirsch')
f_text('ola mundo')
f_text('carro')
f_text('vou ganhar na mega da virada!')