import socket
from rsaMainExample import *
import socket
import threading
import sys
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

key = generateKey()


def sendMsg():
    while True:
        msg = input("")
        encMsg = encryptMessage(publicKey, msg)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time:} {msg}")
        encMsg = encryptMessage(publicKey, msg)
        s.send(encMsg)


def recvMsg():
    while True:
        encMessage = s.recv(1024)
        decMessage = decryptMessage(key.exportKey(), encMessage)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time:} {decMessage.decode()}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CONSOLE] Client connected")

    # reciever publicKey
    publicKey = RSA.importKey(s.recv(1024), passphrase=None)
    print("[CONSOLE] Public key recieved")
    s.send(key.publickey().exportKey(format="PEM", passphrase=None, pkcs=1))
    print("[CONSOLE] You can now start by entering a message\n")
    t = threading.Thread(target=recvMsg)
    t.start()

    sendMsg()
