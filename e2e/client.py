import socket
from e2e.rsaMainExample import *
import socket
import threading
import sys
from datetime import datetime


def sendMsg(s,publicKey,encryptedAESKey,fileHash,ECCkey):
    # Encrypt AES key using recipient's public RSA key
    encMsg = encryptMessage(publicKey, encryptedAESKey)
    # Signing the file with the ECC key -- digital signature
    signature = signingMessage(ECCkey, fileHash)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{current_time:} {encryptedAESKey}")
    # Send encrypted AES key through socket
    s.send(encMsg)
    print(f"{current_time:} {signature}")
    # Send signature through socket -- need check if this needs to be encrypted?
    s.send(signature)
    print("Closing connection")
    s.close()

# Not being used on client side
#def recvMsg(s,key):
#    while True:
#        encMessage = s.recv(1024)
#        decMessage = decryptMessage(key.exportKey(), encMessage)
#        now = datetime.now()
#        current_time = now.strftime("%H:%M:%S")
#        print(f"{current_time:} {decMessage.decode()}")

def startClient(encryptedAESKey,fileHash):
    HOST = "127.0.0.1"
    PORT = 12345
    ECCkey = generateECCKey()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[CONSOLE] Client connected")

        # reciever publicKey
        publicKey = RSA.importKey(s.recv(1024), passphrase=None)
        print("[CONSOLE] Public key recieved")
        # Send public ECC key of client to server
        s.send(ECCkey.public_key().export_key(format="SEC1"))
        # Sending AES Key
        print("[CONSOLE] Sending AES key...\n")
        #t = threading.Thread(target=recvMsg, args=(s,RSAkey,))
        #t.start()
        sendMsg(s,publicKey,encryptedAESKey,fileHash,ECCkey)