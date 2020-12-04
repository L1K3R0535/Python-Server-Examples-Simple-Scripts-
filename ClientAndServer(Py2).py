#!/usr/bin/python
#Server
import socket
name = socket.gethostname()
name = socket.gethostbyname(name)
client = socket.socket()
def conn():
    i=raw_input("Connect('y'|'n')?\nadmin@windowsbox~:$ "); return i
def sendAndRecv(n,c):
    print "Attempting to connect"
    client.connect((n,1234))
    print "Connected to the server.\nTo exit just press ctrl+C"
    while True:
        try:
            content=raw_input("admin@windowsbox~:$ ")
            client.send("%s"%(content))
            i=client.recv(1024)
            print i
        except KeyboardInterrupt:
            print "Ok, closing connection..."
            print "Exiting, see you another time!"
            client.close(); exit()
if conn() == "y":
    print "connecting..."
    sendAndRecv(name,client)
else:
    print "Ok, bye then."
    exit()
#___ END ____
 
#!/usr/bin/python
#Client
import socket
name = socket.gethostname()
name = socket.gethostbyname(name)
client = socket.socket()
def conn():
    i=raw_input("Connect('y'|'n')?\nadmin@windowsbox~:$ "); return i
def sendAndRecv(n,c):
    print "Attempting to connect"
    client.connect((n,1234))
    print "Connected to the server.\nTo exit just press ctrl+C"
    while True:
        try:
            content=raw_input("admin@windowsbox~:$ ")
            client.send("%s"%(content))
            i=client.recv(1024)
            print i
        except KeyboardInterrupt:
            print "Ok, closeing connection..."
            print "Exiting, see you another time!"
            client.close(); exit()
if conn() == "y":
    print "connecting..."
    sendAndRecv(name,client)
else:
    print "Ok, bye then."
    exit()
#____ END ____