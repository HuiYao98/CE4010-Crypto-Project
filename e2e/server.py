import socket
from rsaMainExample import *

HOST = "127.0.0.1"
PORT = 12345


key = generateKey()

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        print("[CONSOLE] Listening...")
        s.listen()

        conn, addr = s.accept()
        with conn:
            print(f"[CONSOLE] connected by {addr}")

            conn.send(key.publickey().exportKey(format="PEM", passphrase=None, pkcs=1))
            encMessage = conn.recv(1024)
            if not encMessage:
                break

            decMessage = decryptMessage(key.exportKey(), encMessage)
            print(decMessage.decode())
