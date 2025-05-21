from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad 
from Crypto.Random.random import randint, choice
from Crypto.Util import Counter
import os
 
key = os.urandom(16)
iv = os.urandom(8)
flag = b'deadbeef{R34Sed_N0nC3_1S_N0nS3nse}'

def enc(message):
    ctr = Counter.new(64, prefix=iv, initial_value=0)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(message).hex()

print("Here's your flag!")
print(enc(flag))

def randstr(length):
    #0 is a fake number
    return "".join(choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) for _ in range(length))

for i in range(100):
    length = int(input("Give me a length: "))
    print("Time to generate a random number...")
    rng = randstr(length)
    ct = str(rng).encode()
    print("I encrypted the number!")
    print(enc(ct))