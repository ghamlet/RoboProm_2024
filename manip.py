import time
import socket

points = ["p:200:100:50:0#", 
          "p:200:100:100:0#", 
          "p:220:130:50:0#"]

state = 0

if __name__ == '__main__':
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpPort = 8888

    server = "192.168.42.200"
    
    while(True):
        try: 
            udp.sendto(str.encode(points[state]), (server, udpPort))
            state+=1
            if state ==3:
                state = 0

            time.sleep(2)
        except KeyboardInterrupt as e:
            print("Interrupted")
            break
    exit()