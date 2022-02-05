import os

sistema = os.environ
print(sistema) # mostra pastas e detalhes dos sistemas em dicionário

print(sistema['USERNAME']) # metodo de mostrar os dados da variavel criada com o os.environ

print(os.getcwd()) # mostra diretório atual

novo_caminho = r"C:\Users\geova\Desktop"
os.chdir(novo_caminho) # usado para mudar de caminho

print(os.getcwd())

#os.mkdir('teste') # cria uma nova pasta
print(os.listdir()) # lista tudo o que há em uma pasta de um caminho atual

caminho = r"C:\Users\geova\Desktop\testeos\pasta01\nova-pasta"
#os.makedirs(caminho) # cria varias pastas uma dentro da outra caso não exista

print(os.listdir())

pasta_rem = r"C:\Users\geova\Desktop\testeos\pasta01\nova-pasta"
#os.rmdir(pasta_rem) # remove pastas se elas estiverem vazias

os.startfile(path="") # abre arquivos dentro de um diretório

os.rename('oi.txt', 'tchau.txt') # renomeia o arquivo, se o usuario estiver na pasta do arquivo

os.remove('tchau.txt') # apaga o arquivo da pasta atual

for root, dirs, files in os.walk(os.getcwd()): # jeito mais complexo de manipular e ver raiz, diretório e arquivos.
    print(root)

os.path.basename(os.getcwd()) # entrega o nome do diretório atual

os.path.commonpath([caminho1, caminho2]) # faz uma comparação e encontra o caminho comum entre os diretórios

os.path.commonprefix([caminho1, caminho2]) # vai até a pasta faz comparação e usa como comum, retirando os prefixos diferentes

os.path.dirname(caminho) # dá ao usuario o caminho direito onde o arquivo está, sem a necessidade de ficar tratando texto.

drive = 'C:'
usuario = 'Alex'
pasta_base = 'Desktop'
caminho = os.path.join(drive, r'\User', usuario, pasta_base) # faz a junção de caminhos, ajuda na manipulação de diretórios
