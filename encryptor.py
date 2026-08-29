KEY = "MySecretKey123"
FILE = "file.txt"
def rc4(data, key):
  
    S = list(range(256))
    j = 0
    
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
    
   
    i = j = 0
    result = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        result.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(result)


print("STEP 1: Opening file.txt in binary mode...")
file = open(FILE, 'rb')

print("STEP 2: Reading file contents into memory buffer...")
data = file.read()
file.close()
print(f"Read {len(data)} bytes")

print("STEP 3: Encrypting data using RC4...")
encrypted_data = rc4(data, KEY)
print(f"Encrypted {len(encrypted_data)} bytes")

print("STEP 4: Writing encrypted data back to file.txt...")
file = open(FILE, 'wb')
file.write(encrypted_data)
file.close()

print("\n✓ ENCRYPTION COMPLETE!")
print("  file.txt now contains encrypted binary data")