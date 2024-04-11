import time
import socket

udpPort = 8888
server = "192.168.42.200"
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pack_coord_high = [260, 113, 250]
pack_coord_low = [260, 113, 220]


delta = 80  #смещение вниз

point_1 = [260, -77, 134]  #задаю верха
point_2 = [240, -70, 100]
point_3 = [260, -77, 134] 
point_4 = [220, 100, 150]
point_5 = [240, -70, 100]
point_6 = [260, -77, 134]


points = [point_1, point_2 ,point_3, point_4 ,point_5, point_6]

points_udp = [[], [], [], [], [],[]]



def generate_udp_packets_to_manip():
    for id, point in enumerate(points):
        
        points_udp[id].append(f"p:{point[0]}:{point[1]}:{point[2]}:0#")
        points_udp[id].append(f"p:{point[0]}:{point[1]}:{point[2]- delta}:0#")
        points_udp[id].append(f"p:{point[0]}:{point[1]}:{point[2]- delta}:1#")
        points_udp[id].append(f"p:{point[0]}:{point[1]}:{point[2]}:1#")
        
        points_udp[id].append(f"p:{pack_coord_high[0]}:{pack_coord_high[1]}:{pack_coord_high[2]}:1#")
        points_udp[id].append(f"p:{pack_coord_low[0]}:{pack_coord_low[1]}:{pack_coord_low[2]}:1#")
        points_udp[id].append(f"p:{pack_coord_low[0]}:{pack_coord_low[1]}:{pack_coord_low[2]}:0#")
        points_udp[id].append(f"p:{pack_coord_high[0]}:{pack_coord_high[1]}:{pack_coord_high[2]}:0#")

    for p in points_udp:
        print(p,"\n")
    
    return points_udp




def move_home():
    pass


def move_manip(cmd):
    udp.sendto(str.encode(cmd), (server, udpPort))
    # time.sleep(2)
        
