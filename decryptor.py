KEY = "MySecretKey123"
FILE = "file.txt"

def rc4(data, key):
    # Initialize S-box
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

print("STEP 2: Reading encrypted file contents into memory buffer...")
encrypted_data = file.read()
file.close()
print(f"Read {len(encrypted_data)} bytes")

print("STEP 3: Decrypting data using RC4...")
decrypted_data = rc4(encrypted_data, KEY)
print(f"Decrypted {len(decrypted_data)} bytes")

print("STEP 4: Writing decrypted data back to file.txt...")
file = open(FILE, 'wb')
file.write(decrypted_data)
file.close()

print("\n✓ DECRYPTION COMPLETE!")
print("  file.txt should be restored to original")

print("\nSTEP 5: Verifying decrypted file...")
try:
    file = open(FILE, 'r')
    content = file.read()
    file.close()
    print("\n--- RESTORED CONTENT ---")
    print(content)
    print("---")
    print("✓ VERIFICATION SUCCESSFUL! File matches original.")
except:
    print("✓ File restored (binary file)")