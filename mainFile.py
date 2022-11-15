from e2e.client import startClient
from e2e.server import startServer, connectClient

from fileAES.AesMain import *
from fileAES.fileEncryptAes import *

print(get_file_hash("testFile.txt"))
while True:
    userInput = input("""Welcome to our secure file transfer service! 
1. Send file
2. Recieve file
3. Exit\n""")
    if userInput == "1":
        print("Starting sending client....")
        IV, key, filenameEncrypt = initializeAESencrypt()
        encrypt_file(key, filenameEncrypt, IV, out_filename=None, chunksize=64*1024)
        startClient(key.decode())
    elif userInput == "2":
        print("Starting server....")
        s, key = startServer()
        nkey = connectClient(s,key)
        nkey, filenameDecrypt = initializeAESdecrypt(nkey)
        decrypt_file(nkey, filenameDecrypt, out_filename=None, chunksize=64*1024)
    elif userInput == "3":
        print("Thank you for using our service!")
        break
    else:
        print("Please input a valid option")
    

