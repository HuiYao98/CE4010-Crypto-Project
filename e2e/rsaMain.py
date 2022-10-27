from turtle import pu
from Crypto import Random
import rsa
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generateKey():
   #number of bits, how many processes to run in parallel
   (publicKey,privateKey) = rsa.newkeys(512)
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

main()