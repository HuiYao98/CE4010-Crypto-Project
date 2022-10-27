import socket
from rsaMain import *
HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print("connected")
    data =s.recv(1024)
    msg =encryptMessage(data, "Boombs!")
    s.send(msg)


