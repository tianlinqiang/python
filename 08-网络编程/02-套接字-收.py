from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("",6789))
while True:
		recvData = udpSocket.recvfrom(1024)
		content , destInfo = recvData
		print("content is %s" %content.decode("utf-8"))
