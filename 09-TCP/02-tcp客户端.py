from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 8989))

clientSocket.send("haha".encode("utf-8"))

recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData)
clientSocket.close()
