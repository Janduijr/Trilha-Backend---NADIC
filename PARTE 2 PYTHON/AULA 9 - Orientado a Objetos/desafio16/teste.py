import hashlib

senha = 'Jandui'
cod = senha.encode('utf-8')
hash = hashlib.sha256(cod).hexdigest()

print(hash)