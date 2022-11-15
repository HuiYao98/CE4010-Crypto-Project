from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import secrets
from fileAES.fileEncryptAes import decrypt_file, encrypt_file, get_file_hash

def generateAESkey():
    # Random key generated here using secrets module - 32 byte key for AES-256, https://docs.python.org/3/library/secrets.html
    # but secrets module generate 1.3 characters using this function due to base64 encoding, so put 24 byte
    key = secrets.token_urlsafe(24)
    key = key.encode(encoding="utf8", errors="replace")
    return key

def initializeAESencrypt():
    # Get filename to encrypt
    filename = input("What is the filename that you want to encrypt?")
    # Initialization vector - random IV using crypto random - 16 bytes
    IV = get_random_bytes(16)   
    # Generate AES key
    key = generateAESkey()

    return IV, key, filename

def initializeAESdecrypt(key):
    # Get filename to encrypt
    filename = input("What is the filename that you want to decrypt?")    
    # Convert AES key from string to utf8
    key = key.encode("utf8")

    return key, filename


