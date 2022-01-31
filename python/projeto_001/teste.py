from Randomtest import filtro_nrepeat, reverse_str

lista_teste = ['alex hirsch', 'camila cristo', 'vera lucia hirsch']
n = filtro_nrepeat(lista_teste)

reverse_str(n)

import hashlib

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

hash_string = 'alexclear'
sha_signature = encrypt_string(hash_string)
print(sha_signature)
