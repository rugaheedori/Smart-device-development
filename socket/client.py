import socket
from time import sleep

testSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

ip = "127.0.0.1"
port = 9999

bConn = 0
while not bConn:
    try:
        print("> Connecting to the server ...")
        testSocket.connect((ip, port))
        sleep(0.5)
        bConn = 1
    except socket.error as e:
        print("Error/Socket "+str(e))
        sleep(1)
        continue
print("> Server connected!!")

while 1:
    no = int(input("> Data to send to the server? "))
    testSocket.send(no.to_bytes(1, 'big'))
    print("> Waiting for data from the server...")
    msg = testSocket.recv(1)
    print("> Received data from client =", int.from_bytes(msg, "big"))