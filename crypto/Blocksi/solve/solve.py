from Crypto.Cipher import AES 
key = iv = b'deadbeefdeadbeef'
enc = bytes.fromhex("60e000d1b9bb2d5600848d8c1af8ac43b16c6f2ba1b057de89591c30baca7931")
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
print(cipher.decrypt(enc))