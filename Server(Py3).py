#!/usr/bin/python3
#Server
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1234
address=(ip,port)
server.bind(address)
server.listen(5)
print("[+] Started listening on",ip,":",port)
client,addr = server.accept()
print("[*] Got a connection from ",addr[0],":",addr[1])
class _data_:
    def send(self):
        client.send(bytes(self,"utf-8"))
while True:
    data = client.recv(1024)
    print("[+] From the client: "+str(data))
    print("Processing data")
    if str(data) == "b'hello server'" or str(data) == "b'Hello server'":
        _data_.send("hello client!")
        #client.send(bytes("Hello client!\n","utf-8"))
        print("processing done.\n Response sent.")
    elif data == "close":
        client.send(bytes("Goodbye!\n","utf-8")); server.close()
    else:
        client.send(bytes("Invalid data","utf-8"))
        print("Response sent: invalid data.")
#___ END ___
