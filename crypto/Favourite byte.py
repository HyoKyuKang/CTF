def xor_decrypt(hex_string):
    # Step 1: Convert the hex string to bytes
    encrypted_bytes = bytes.fromhex(hex_string)
    
    # Step 2: Brute force every possible single-byte XOR key (0x00 to 0xFF)
    for key in range(256):
        # XOR each byte with the key
        decrypted_bytes = bytes([b ^ key for b in encrypted_bytes])
        
        # 출력 (바이트 형태 또는 ASCII 문자열로 시도)
        try:
            # 가능한 ASCII 문자로 변환하여 출력
            print(f"Key: {key} - Message: {decrypted_bytes.decode('ascii')}")
        except UnicodeDecodeError:
            # 만약 ASCII로 변환할 수 없는 경우 바이트 그대로 출력
            continue

# Given hex string
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
xor_decrypt(hex_string)
