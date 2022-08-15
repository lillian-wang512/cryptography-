from nacl.secret import SecretBox

k='11111.doc.symmetric_key'#对称密钥

with open(k, 'rb') as f:
    sy_key = f.read()

file='11111.doc.encrypted'#加密文件
with open(file, 'rb') as c:
    message = c.read()

def symmetric_decrypt(symmetric_key: bytes, ciphertext: bytes):
    return SecretBox(symmetric_key).decrypt(ciphertext)

content=symmetric_decrypt(sy_key,message)

with open('file.doc','wb') as fp:#存储文件
    fp.write(content)
