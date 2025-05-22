from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad 
from hashlib import sha256
import os
 
key = os.urandom(16)
secret = os.urandom(16)
flag = b'deadbeef{REDACTED}'
cipher = AES.new(key, AES.MODE_ECB)

def enc(message):
    #making sure the length of message is a multiple of 16
    message = pad(message, 16)
    if b"crypto" in message:
        print("you thought")
        exit(0)
    ct = cipher.encrypt(message).hex()
    #https://en.wikipedia.org/wiki/SHA-2
    hashed = sha256(secret + message).hexdigest()
    return (ct, hashed)

#by the way, ct stands for ciphertext (encrypted result)
def dec(ct, hashed):
    plaintext = cipher.decrypt(bytes.fromhex(ct))
    if sha256(secret + plaintext).hexdigest() == hashed:
        return plaintext
    else:
        return b"haha you thought"

print("You get one chance")
inp = bytes.fromhex(input("Give me some text to encrypt (in hex)"))
print(f"{enc(inp) = }")

ct = input("Now give me an encrypted message(in hex): ")
hashed = input("Give me the hash (in hex): ")

if b"crypto" in dec(ct, hashed):
    print("Wow!")
    print(flag)
else:
    print("...")
    exit(0)