from Crypto.Cipher import AES
from fileEncryptAes import decrypt_file, encrypt_file

# Define key here
key = "0123456789abcdef"
# Initialization vector
IV = 16 * "\x00"       
# AES Mode    
mode = AES.MODE_CBC

# Text to encrypt/decrypt -- haven't added
text = 'hello world 1234'

# Encrypting text
encryptor = AES.new(key.encode("utf8"), mode, IV=IV.encode("utf8"))
ciphertext = encryptor.encrypt(text.encode("utf8"))
print(ciphertext)

# Decrypting text
decryptor = AES.new(key.encode("utf8"), mode, IV=IV.encode("utf8"))
plain = decryptor.decrypt(ciphertext)
print(plain)