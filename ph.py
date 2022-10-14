from Crypto.Cipher import AES
from Crypto import Random

import base64
import hashlib


key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
bs = AES.block_size
def _pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def _unpad(s):
    return s[:-ord(s[len(s)-1:])]
    
def encrypt(raw):
    raw = _pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode()))

def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
    
a = encrypt('hi')
pp = a.decode('utf-8')

b= decrypt(pp.encode('utf-8'))
print(b)
    
    