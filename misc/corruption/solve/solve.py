from pwn import * 
# p = process("python3 server.py", shell=True)
p = connect("159.223.73.72", 2000)
p.recvline()
flag = bytes.fromhex(p.recvline().decode())
length = len(flag)
vals = [[] for _ in range(length)]
for i in range(100):
    p.sendline(str(length).encode())
    p.recvline()
    p.recvline()
    ret = bytes.fromhex(p.recvline().strip().decode())
    assert(len(ret) == length)
    for j in range(length):
        vals[j].append(ret[j])
nw = []
for i in range(length):
    nw.append(list(set(vals[i])))
for i in range(length):
    assert(len(nw[i]) == 9)
val = 0
for i in range(1, 10):
    val ^= ord(str(i))
stream = []
for i in range(length):
    cur = 0
    for j in range(9):
        cur ^= nw[i][j]
    cur ^= val 
    stream.append(cur)
stream = bytes(stream)
print(xor(stream, flag))