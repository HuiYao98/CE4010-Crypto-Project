import socket
from rsaMainExample import *

HOST = "127.0.0.1"
PORT = 12345

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[CONSOLE] Client connected")

        msg = input("[CONSOLE] Please enter a message\n")
        if not msg:
            print("[CONSOLE] Client Exiting")
            break
        # reciever publicKey
        publicKey = RSA.importKey(s.recv(1024), passphrase=None)

        encMsg = encryptMessage(publicKey, msg)
        s.send(encMsg)
