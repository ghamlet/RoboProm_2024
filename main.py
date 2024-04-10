import lamp
import pult

import socket
import time
import re

if __name__ == '__main__':
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    NanoPiServer = ("192.168.0.69", 8888)
    udp.bind(NanoPiServer)
    print("Server start")
    
    while True:
        try:
            data, addr = udp.recvfrom(1024)
           
            print("Received message:", data, "from:", addr)
            time.sleep(2)




        except KeyboardInterrupt as e:
            print("Interrupted")
            break
    exit()