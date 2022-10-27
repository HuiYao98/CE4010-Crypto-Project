from Crypto.Cipher import AES
from fileAES.fileEncryptAes import decrypt_file, encrypt_file

# Define key here
key = "0123456789abcdef".encode("utf8")
# Initialization vector
IV = (16 * "\x00").encode("utf8")       
# AES Mode    
mode = AES.MODE_CBC

# Filename to encrypt:
in_filenameEncrypt = "testFile.txt"
#encrypt_file(key, in_filenameEncrypt, IV, out_filename=None, chunksize=64*1024)

# Filename to decrypt:
in_filenameDecrypt = "testFile.txt.enc"
#decrypt_file(key, in_filenameDecrypt, out_filename=None, chunksize=64*1024)