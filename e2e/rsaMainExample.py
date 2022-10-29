from turtle import pu
from Crypto import Random
from Crypto.PublicKey import RSA

from Crypto.Cipher import PKCS1_OAEP

import binascii


# Generate RSA key pair
def generateKey():
    key = RSA.generate(1024)
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


"""
import rsa
def generateKey():
   #number of bits, how many processes to run in parallel
   (publicKey,privateKey) = rsa.newkeys(2048)
   return publicKey, privateKey

def encryptMessage(publicKey, message):
   #encode message in utf8 format
   message = str(message).encode("utf8")
   encryptMessage = rsa.encrypt(message, publicKey)
   return encryptMessage

def decryptMessage(privateKey,encryptedMessage):
   message = rsa.decrypt(encryptedMessage,privateKey)
   print(message.decode('utf8'))


def main():
   (publicKey, privateKey)=generateKey()
   encryptedMessage = encryptMessage(publicKey,"Hello World")
   print(encryptedMessage)
   decryptMessage(privateKey, encryptedMessage)

"""
