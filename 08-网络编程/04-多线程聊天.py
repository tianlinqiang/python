from threading import Thread
from socket import *

def sendData():
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("utf-8"), (destIp, destPort))

def reacData():
	while True:
		recvInfo = udpSocket.recvfrom(1024)	
		print(recvInfo)
		print("\r>>[%s]:%s"%(str(recvInfo[1]),recvInfo[0].decode("utf-8")))
		print("\r<<",end="")
udpSocket = None
destIp = ""
destPort = 0
def main():
    global udpSocket
    global destIp
    global destPort
    
    destIp = input("对方的IP：")
    destPort = int(input("对方的端口号："))
    
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(("",6789))
    
    ts = Thread(target = sendData)
    tr = Thread(target = reacData)

    ts.start()
    tr.start()

    ts.join()
    tr.join()
if __name__=="__main__":
    main()

