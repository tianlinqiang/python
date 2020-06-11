from socket import *
def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(("",8888))
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print("[%s]:%s"%(str(recvInfo[1]),recvInfo[0].decode("utf-8")))
if __name__=="__main__":
    main()
