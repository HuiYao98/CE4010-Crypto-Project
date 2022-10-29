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

        msg = input()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time:} {msg}")
        encMsg = encryptMessage(publicKey, msg)
        conn.send(encMsg)


def recvMsg():
    while True:
        try:
            encMessage = conn.recv(1024)
            decMessage = decryptMessage(key.exportKey(), encMessage)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{current_time:} {decMessage.decode()}")
        except OSError:
            continue


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    print("[CONSOLE] Listening...")
    s.listen()
    conn, addr = s.accept()
    print(f"[CONSOLE] connected by {addr}")
    conn.send(key.publickey().exportKey(format="PEM", passphrase=None, pkcs=1))

    print("[CONSOLE] Recieved Key")
    publicKey = RSA.importKey(conn.recv(1024), passphrase=None)
    print("[CONSOLE] You can now start by entering a message\n")
    t = threading.Thread(target=recvMsg)
    t.start()

    sendMsg()
