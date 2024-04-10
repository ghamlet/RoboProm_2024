import lamp
import pult

import socket
import time
import re


adreses = {
    "core": "192.168.42.241",
    "lamp": "192.168.42.10",
    "pult" :"192.168.42.88",
    "manip" :"192.168.42.200"
}


if __name__ == '__main__':
    udp_hand = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    NanoPiServer = ("192.168.0.69", 8888)
    udp_hand.bind(NanoPiServer)
    print("Server start")
    
    while True:
        try:
            data, addr = udp_hand.recvfrom(1024) # addr contains the IP address of the device that sent the message and port
            
            print("Received message:", data.decode(), "from:", addr)

            udp_sender.sendto(str.encode("coci"), ("192.168.0.80", 8888))


            time.sleep(2)




        except KeyboardInterrupt as e:
            print("Interrupted")
            break
    exit()