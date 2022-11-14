import socket
from e2e.rsaMainExample import *
import socket
import threading
import sys
from datetime import datetime


def sendMsg(s,publicKey,encryptedAESKey):
    encMsg = encryptMessage(publicKey, encryptedAESKey)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{current_time:} {encryptedAESKey}")
    s.send(encMsg)
    print("Closing connection")
    s.close()


def recvMsg(s,key):
    while True:
        encMessage = s.recv(1024)
        decMessage = decryptMessage(key.exportKey(), encMessage)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time:} {decMessage.decode()}")

def startClient(encryptedAESKey):
    HOST = "127.0.0.1"
    PORT = 12345
    RSAkey = generateKey()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[CONSOLE] Client connected")

        # reciever publicKey
        publicKey = RSA.importKey(s.recv(1024), passphrase=None)
        print("[CONSOLE] Public key recieved")
        #s.send(RSAkey.publickey().exportKey(format="PEM", passphrase=None, pkcs=1))
        print("[CONSOLE] Sending AES key...\n")
        #t = threading.Thread(target=recvMsg, args=(s,RSAkey,))
        #t.start()
        sendMsg(s,publicKey,encryptedAESKey)