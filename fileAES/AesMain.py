from Crypto.Cipher import AES
from fileAES.fileEncryptAes import decrypt_file, encrypt_file

def generateAESkey():
    # Define key here -- need to come up with key generation algo thats random
    key = "0123456789abcdef".encode("utf8")
    return key

def initializeAESencrypt():
    # Get filename to encrypt
    filename = input("What is the filename that you want to encrypt?")
    # Initialization vector
    IV = (16 * "\x00").encode("utf8")       
    # Generate AES key
    key = generateAESkey()

    return IV, key, filename

def initializeAESdecrypt(key):
    # Get filename to encrypt
    filename = input("What is the filename that you want to decrypt?")    
    # Convert AES key from string to utf8
    key = key.encode("utf8")

    return key, filename

# Filename to encrypt:
#in_filenameEncrypt = "testFile.txt"
#encrypt_file(key, in_filenameEncrypt, IV, out_filename=None, chunksize=64*1024)

# Filename to decrypt:
#in_filenameDecrypt = "testFile.txt.enc"
#decrypt_file(key, in_filenameDecrypt, out_filename=None, chunksize=64*1024)

