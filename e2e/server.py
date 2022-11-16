import socket
from e2e.rsaMainExample import *
import socket
import ssl
import threading
import sys

from datetime import datetime


def sendMsg(conn,publicKey):
    while True:
        msg = input()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time:} {msg}")
        encMsg = encryptMessage(publicKey, msg)
        conn.send(encMsg)


def recvMsg(conn,key):
    try:
        # Get encoded AES key from client
        encMessage = conn.recv(1024)
        # Get signature from client
        signature = conn.recv(256)
        # Decrypt AES key with private RSA key
        decMessage = decryptMessage(key.exportKey(), encMessage)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time:} {decMessage.decode()}")
        return decMessage.decode(),signature
    except OSError:
        pass

def connectClient(s, key):
    recieveFile = input("Do you want to recieve a file?")
    if recieveFile == "Y":
        print("Connecting to client....")
        s.listen()
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile="e2e\server-public-key.pem", keyfile="e2e\server-private-key.pem")
        conn, addr = s.accept()
        conn2 = context.wrap_socket(conn, server_side=True)
        print(f"[CONSOLE] connected by {addr}")
        # Send own RSA public key to client
        conn2.send(key.publickey().exportKey(format="PEM", passphrase=None, pkcs=1))
        print("[CONSOLE] Sent Public Key")
        # Get ECC public key of client -- for signature signing -- using ECC-256
        publicKey = ECC.import_key(conn2.recv(256), passphrase=None, curve_name="P-256")

        # Used to wait and recieve key & signature from client
        AESkey, signature = recvMsg(conn2,key)

        # Close socket connection after recieving key
        s.close()

        return AESkey, publicKey, signature
    else:
        s.close()

def startServer():
    #Set IP address & port that the server listens to -- if host is "", means listen to any ip address
    HOST = "127.0.0.1"
    PORT = 12345
    # Generate public key on server side
    key = generateKey()
    # Create socket obj and bind to ip/port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("[CONSOLE] Listening...")
    return s, key
            