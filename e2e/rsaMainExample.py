from turtle import pu
from Crypto import Random
from Crypto.PublicKey import RSA, ECC
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import DSS

import binascii


# Generate RSA key pair
def generateKey():
    key = RSA.generate(1024)
    return key

# Generate ECC key pair - https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html#
def generateECCKey():
   key = ECC.generate(curve='P-256')
   return key

# encrypting the data using RSA, sender publickey
# PKCS1_OAEP is an asymetric chipher base on RSA and OAEP padding
# Please note the warning! digital signature? to ensure legitamacy of message?
# refer here for more info:https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
def encryptMessage(publicKey, message):
    cipher_rsa = PKCS1_OAEP.new(publicKey)
    # type casting message to bytes
    message = bytes(message, "utf-8")
    return cipher_rsa.encrypt(message)


# decrypting the data using RSA, reciever private key
def decryptMessage(privateKey, message):
    # importing the private key object
    privateKey = RSA.import_key(privateKey)
    cipher_rsa = PKCS1_OAEP.new(privateKey)
    return cipher_rsa.decrypt(message)

# Use for signing message using ECDSA - https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html 
def signingMessage(key, hash):
   signer = DSS.new(key, 'fips-186-3')
   signature = signer.sign(hash)
   return signature

# Use for verify message using ECDSA
def verifyMessage(key, hash, signature):
   verifier = DSS.new(key, 'fips-186-3')
   try:
      verifier.verify(hash, signature)
      return 1
   except ValueError:
      return 0
