#coding = utf-8
# -*- coding: UTF-8 -*-
from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

destIp = input("请输入IP地址：")

destPort = int(input("请输入端口号："))
while True:
    destData = input("请输入要发送的内容：")

    udpSocket.sendto(destData.encode('utf-8'), (destIp, destPort))
