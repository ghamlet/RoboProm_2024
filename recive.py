import time
import socket
import re

if __name__ == '__main__':
    ip = "192.168.42.241"
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpPort = 8888
    udp.bind((ip, udpPort))
    
    while(True):
        try:
            data, addr = udp.recvfrom(1024)
           
            print("received message: %s" % data)
            time.sleep(2)
        except KeyboardInterrupt as e:
            print("Interrupted")
            break
    exit()