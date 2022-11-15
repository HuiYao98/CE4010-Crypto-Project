import socket
from e2e.rsaMainExample import *
import socket
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
        encMessage = conn.recv(1024)
        # Private Key is here
        decMessage = decryptMessage(key.exportKey(), encMessage)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time:} {decMessage.decode()}")
        return decMessage.decode()
    except OSError:
        pass

def connectClient(s, key):
    recieveFile = input("Do you want to recieve a file?")
    if recieveFile == "Y":
        print("Connecting to client....")
        s.listen()
        conn, addr = s.accept()
        print(f"[CONSOLE] connected by {addr}")
        #Send public key to client
        conn.send(key.publickey().exportKey(format="PEM", passphrase=None, pkcs=1))
        print("[CONSOLE] Sent Public Key")
        # Get public key of client
        publicKey = RSA.importKey(conn.recv(1024), passphrase=None)

        # Used to wait and recieve key from client
        key = recvMsg(conn,key)

        # Close socket connection after recieving key
        s.close()

        return key
        # Used for multiple threaded message recieving --> not needed
        #t = threading.Thread(target=recvMsg, args=(conn,key,))
        #t.start()

        #sendMsg(conn,publicKey)
        #t = threading.Thread(target=connectClient, args=(key,s,))
        #t.start()
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

    # Old code -- not needed currently
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #    s.bind((HOST, PORT))
    #    print("[CONSOLE] Listening...")
    #    return s, key
            