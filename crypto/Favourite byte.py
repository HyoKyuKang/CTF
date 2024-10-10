def xor_decrypt(hex_string):
    # Step 1: Convert the hex string to bytes
    encrypted_bytes = bytes.fromhex(hex_string)
    
    # Step 2: Brute force every possible single-byte XOR key (0x00 to 0xFF)
    for key in range(256):
        # XOR each byte with the key
        decrypted_bytes = bytes([b ^ key for b in encrypted_bytes])
        
        # 모든 바이트가 가독성 있는 ASCII 범위(32~126)에 있는지 확인
        if all(32 <= b <= 126 for b in decrypted_bytes):
            # ASCII로 변환하여 출력
            try:
                print(f"Key: {key} - Message: {decrypted_bytes.decode('ascii')}")
            except UnicodeDecodeError:
                continue  # 디코딩 오류가 발생하면 건너뜀

# Given hex string
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
xor_decrypt(hex_string)
