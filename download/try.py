from nacl.signing import VerifyKey

key='public_key'
with open(key, 'rb') as f:
    pk = f.read()

file_s='aim.doc.sig'#签名文件
with open(file_s, 'rb') as f:
    signature = f.read()

file='aim.doc.encrypted'#加密文件
with open(file, 'rb') as f:
    message = f.read()

def verify(message:bytes,signature: bytes):
    return VerifyKey(pk).verify(message,signature)

content=verify(message,signature)
print("验签成功！")





