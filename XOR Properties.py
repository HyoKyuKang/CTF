from Crypto.Util.number import *

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
x = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
y = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# 바이트 데이터를 정수로 변환
KEY1 = int.from_bytes(KEY1, byteorder='big')
x = int.from_bytes(x, byteorder='big')
y = int.from_bytes(y, byteorder='big')
flag = int.from_bytes(flag, byteorder='big')

# KEY2와 KEY3 계산
KEY2 = x ^ KEY1
KEY3 = y ^ KEY2

# flag 복호화
flag ^= KEY1 ^ KEY2 ^ KEY3

# 결과 출력: 바이트로 변환할 때는 길이를 지정
flag_bytes = flag.to_bytes((flag.bit_length() + 7) // 8, byteorder='big')
print(flag_bytes.decode('utf-8'))
