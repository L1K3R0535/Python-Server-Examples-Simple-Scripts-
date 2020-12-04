#!/usr/bin/python3
#Client
import socket, sys
name = socket.gethostname()
name = socket.gethostbyname(name)
client = socket.socket()
def tcontc():
    i=input("Connect('y'|'n')?\nadmin@%sbox~:$ "%(sys.platform)); return i
def sendAndRecv(n,c):
    print("Attempting to connect")
    client.connect((n,1234))
    print("Connected to the server.\nTo exit just press ctrl+C")
    while True:
        try:
            content=input("admin@%sbox~:$ "%(sys.platform))
            client.send(bytes(content,"utf-8"))
            i=client.recv(1024)
            print(str(i))
            if content == "close":
                client.close()
        except KeyboardInterrupt:
            print("Ok, closing connection...")
            print("Exiting, see you another time!")
            client.close(); exit()
if tcontc() == "y":
    print("connecting...")
    sendAndRecv(name,client)
else:
    print("Ok, bye then.")
    exit()
#___ END ___