from e2e.client import startClient
from e2e.server import startServer, connectClient
from e2e.rsaMainExample import verifyMessage

from fileAES.AesMain import *

while True:
    userInput = input(
        """Welcome to our secure file transfer service! 
1. Send file
2. Recieve file
3. Exit:\n"""
    )
    if userInput == "1":

        print("Starting sending client....")
        # Get AES parameters (ie. Key, IV and filename to encrypt)
        IV, AESkey, filenameEncrypt = initializeAESencrypt()
        print("AES Key before encryption:", AESkey)
        # Generate hash for the target file -- Used for DSS signature
        fileHash = get_file_hash(filenameEncrypt)
        print("File Hash:", fileHash.hexdigest())

        # Encrypt the file using AES
        encrypt_file(
            AESkey, filenameEncrypt, IV, out_filename=None, chunksize=64 * 1024
        )
        print("File encrypted! Sending key to server....")
        # Start client for sending AES key to server
        startClient(AESkey.decode(), fileHash)

    elif userInput == "2":
        print("Starting server....")

        # Get socket and RSA public key for server side
        s, RSAkey = startServer()

        # Sending public key to client, and recieving AES key, and ECC public key + signature for digital signature verification
        AESkey, ECCpubKey, signature = connectClient(s, RSAkey)

        # Get AES parameters (ie. Key - just converting to required format, IV and filename to decrypt)
        AESkey, filenameDecrypt = initializeAESdecrypt(AESkey)

        # Decrypt the file using AES key recieved
        filename = decrypt_file(
            AESkey, filenameDecrypt, out_filename=None, chunksize=64 * 1024
        )

        # print out the text of file
        with open(filename, "rb") as plaintext:
            print("File contents:", plaintext.read())
            
        # Generate hash for the file that was recieved -- Used for DSS signature
        fileHash = get_file_hash(filename)

        # Verifying that the file is signed legitimately
        verified = verifyMessage(ECCpubKey, fileHash, signature)
        if verified == 1:
            print("File is authentic")
        elif verified == 0:
            print("File is not authentic/has been tampered with :(")

    elif userInput == "3":
        print("Thank you for using our service!")
        break
    else:
        print("Please input a valid option")
