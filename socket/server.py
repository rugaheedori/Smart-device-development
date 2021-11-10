import socket
from typing import Text

hostServer = "127.0.0.1"
portServer = 8080
server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostServer, portServer))
server.listen(5)
print("*Waiting for clients - !")
serverSock, addr = server.accept()
print("*A clinet(", addr, ") conndected - ! : ")

def deleteOverlapCharacter(msg) : 
    array = [];
    for i in range (len(msg)) :
        if (msg[i] in array):
            continue
        array.append(msg[i])
    return "".join(array)
while 1:
    print("*Wating for data from the client - !")
    dataFromClient = serverSock.recv(1024)
    print("*Received data from the client = ", dataFromClient.decode())
    print("*Data to send to the client - !")
    serverSock.send(deleteOverlapCharacter(dataFromClient.decode()).encode())

