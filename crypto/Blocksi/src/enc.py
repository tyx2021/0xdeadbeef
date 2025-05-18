from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad 
flag = b'deadbeef{1_L0Ve_Bl0Ck_CIpH3rS}'
flag = pad(flag, 16)
key = b'deadbeefdeadbeef'
iv = b'deadbeefdeadbeef'
cipher = AES.new(key, mode=AES.MODE_CBC, iv=iv)
print(cipher.encrypt(flag).hex())