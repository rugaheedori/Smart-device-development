import socket
from time import sleep

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

ip = "127.0.0.1"
port = 8080

bConn = 0
while not bConn:
    try:
        print("*Connecting to the server - !")
        clientSocket.connect((ip, port))
        sleep(0.5)
        bConn = 1
    except socket.error as e:
        print("Error/Socket "+str(e))
        sleep(1)
        continue
print("* Server connected - !")

while 1:
    text = input("# Data to send to the server?")
    clientSocket.send(text.encode())
    print("> Waiting for data from the server...")
    dataFromServer = clientSocket.recv(1024)
    print("> Received data from client =", dataFromServer.decode())