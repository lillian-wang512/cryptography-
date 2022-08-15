from hashlib import sha512

with open('aim.doc', 'rb') as f:
    file = f.read()

hash_value = sha512(file).hexdigest()
with open('aim.doc.hash', 'rb') as s:
    file_s = s.read()

hash_origin=str(file_s,'utf-8')
if hash_origin==hash_value:
    print('Successfully!')
else:
    print('Abandon!')