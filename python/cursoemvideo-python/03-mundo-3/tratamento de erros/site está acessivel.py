import urllib.request

try:
    url = urllib.request.urlopen('https://www.arvore.com.br/')
except:
    print('deu erro')
else:
    print('tudo ok')
