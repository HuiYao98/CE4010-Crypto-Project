import socket
from e2e.rsaMainExample import *
import socket
import ssl
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
    print(f"{current_time:} {encMsg}")
    # Send encrypted AES key through socket
    s.send(encMsg)
    #print(f"{current_time:} {signature}")
    # Send signature through socket -- need check if this needs to be encrypted?
    s.send(signature)
    print("[CONSOLE] Sent!")
    print("[CONSOLE] Closing connection...")
    s.close()

def startClient(encryptedAESKey,fileHash):
    HOST = "127.0.0.1"
    PORT = 12345
    ECCkey = generateECCKey()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations("e2e\ca-keys.pem")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        ss = context.wrap_socket(s, server_hostname="localhost")
        ss.connect((HOST, PORT))
        print("[CONSOLE] Client connected")
        # Reciever publicKey
        publicKey = RSA.importKey(ss.recv(1024), passphrase=None)
        print("[CONSOLE] Public key recieved")
        # Send public ECC key of client to server
        ss.send(ECCkey.public_key().export_key(format="SEC1"))
        # Sending AES Key
        print("[CONSOLE] Sending AES key...\n")
        sendMsg(ss,publicKey,encryptedAESKey,fileHash,ECCkey)