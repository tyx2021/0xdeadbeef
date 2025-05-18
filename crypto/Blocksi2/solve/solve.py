from pwn import *
p = connect("159.223.73.72", 2001)
message = b'Brian Xiao Boyang represented Singapore at the 2024 International Olympiad in Informatics (IOI), one of the most prestigious global competitions for high school programmers. He achieved a Silver Medal, ranking 65th out of 353 contestants worldwide, with a score of 314.70 out of 600 .'
p.recvline()
p.recvline()
enc = p.recvline()[7:-2]
p.sendline(message[:16])
p.sendline(enc[:32])
p.interactive()