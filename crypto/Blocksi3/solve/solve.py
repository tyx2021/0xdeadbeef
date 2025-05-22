#https://github.com/iagox86/hash_extender
#i cloned this repo into the hash_extender folder

from pwn import *
from Crypto.Util.Padding import pad 
from hashlib import sha256
from subprocess import check_output

secret = b'x'*16
def ext(hash, pt, add):
    from subprocess import check_output

def ext(original_hash: str, pt: bytes, add: bytes, secret_len: int = 16):
    cmd = f"""
    ./hash_extender/hash_extender \
    --data-format=hex \
    --append-format=hex \
    --data {pt.hex()} \
    --append {add.hex()} \
    --signature {original_hash} \
    --secret {secret_len} \
    --format sha256
    """
    
    output = check_output(cmd, shell=True).decode()
    new_sig = None
    new_msg = None
    
    for line in output.splitlines():
        if line.startswith("New signature:"):
            new_sig = line.split(": ")[1].strip()
        if line.startswith("New string:"):
            new_msg = bytes.fromhex(line.split(": ", 1)[1])
    
    return (new_msg, new_sig)

require = ext("a"*64, pad(b"B"*128, 16), b'a')[0][:-1]
#ensure the text has length exactly 128
require = require[128:]
send = b'o'+b"A"*15+b"A"*11+b"crypt"+require+b"A"*(128-len(require)-32)
conn = connect("159.223.73.72", 2006)
# conn = process("python3 server.py", shell=True)
conn.sendline(send.hex())
conn.recvuntil(b"= ")
enc, hashed = eval(conn.recvline())
enc = bytes.fromhex(enc)
newpt, newhash = ext(hashed, pad(send, 16), b"A"*11+b"crypt"+b'o'+b"A"*15)
newenc = enc[:-16] + enc[32:32+len(require)] +enc[16:32]+enc[:16]
conn.sendline(newenc.hex())
conn.sendline(newhash)
conn.interactive()