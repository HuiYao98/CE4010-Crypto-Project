import socket
from rsaMain import *

HOST = '127.0.0.1'
PORT = 12345


(publicKey, privateKey)=generateKey()

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        
        s.bind((HOST,PORT))
        s.listen()

        conn, addr = s.accept()
        with conn:
            print(f"connected by {addr}")
            while True:
                conn.send(publicKey)
                data =conn.recv(1024)
                if not data:
                    break
                data = decryptMessage(privateKey,data)
                print(data)
            