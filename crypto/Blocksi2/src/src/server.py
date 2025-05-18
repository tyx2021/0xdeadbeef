from Crypto.Cipher import AES 
import os 
flag = b'deadbeef{3cB_P3g71N_m0M3Nt}'
def pad(message, blk):
    length = len(message)
    return message + b"\x00" * ((-length) % blk)
key = os.urandom(16)
message = b'Brian Xiao Boyang represented Singapore at the 2024 International Olympiad in Informatics (IOI), one of the most prestigious global competitions for high school programmers. He achieved a Silver Medal, ranking 65th out of 353 contestants worldwide, with a score of 314.70 out of 600 .'
cipher = AES.new(key, mode=AES.MODE_ECB)
enc = cipher.encrypt(pad(message, 16)).hex()
print("I encrypted a message.")
print(f"{message = }")
print(f"{enc = }")
print("Give me a message, and the encrypted value to prove you know the key!")
msg = input("What's the message? ").strip().encode()
ct = input("What's the encrypted message? (in hex) ").strip()
if cipher.encrypt(pad(msg, 16)).hex() == ct:
    if msg == message:
        print("You thought you could trick me...")
    else:
        print("Here's your flag!")
        print(flag)
else:
    print(cipher.encrypt(pad(msg, 16)).hex())
    print("Error: no match")