import time
import socket


class Manipulator:

    def __init__(self, server_address_port):
        self.server_address_port = server_address_port
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def generate_udp_packets_to_manip(self):
        """Для каждой позиции томидора необходимо задать 8 точек манипулятора"""

        self.points_udp = []
        self.points = [
            [178, 1, 240],  # верхние координаты каждой позиции
            [164, -54, 240],
            [225, -14, 240],
            [210, -63, 240],
            [273, -24, 240],
            [260, -79, 240]
        ]

        self.drop_high = 100  # смещение вниз
        self.pack_coord_high = [260, 113, 250]
        self.pack_coord_low = [260, 113, 220]

        for id, point in enumerate(self.points):
            self.points_udp.append([
                f"p:{point[0]}:{point[1]}:{point[2]}:0#",
                f"p:{point[0]}:{point[1]}:{point[2]- self.drop_high}:0#",
                f"p:{point[0]}:{point[1]}:{point[2]- self.drop_high}:1#",
                f"p:{point[0]}:{point[1]}:{point[2]}:1#",

                f"p:{self.pack_coord_high[0]}:{self.pack_coord_high[1]}:{self.pack_coord_high[2]}:1#",
                f"p:{self.pack_coord_low[0]}:{self.pack_coord_low[1]}:{self.pack_coord_low[2]}:1#",
                f"p:{self.pack_coord_low[0]}:{self.pack_coord_low[1]}:{self.pack_coord_low[2]}:0#",
                f"p:{self.pack_coord_high[0]}:{self.pack_coord_high[1]}:{self.pack_coord_high[2]}:0#"  ])

        for p in self.points_udp:
            print(p, "\n")

        return self.points_udp


    def move_home(self):
        """Стартовая позиция манипулятора где он не будетмешаться"""
        self.move_manip([210, -63, 240])


    def move_manip(self, xyz: list, pump: bool = False):
        """Формирует пакет формата p:x:y:z:pump# для отправки на манипулятор на полученных числовых координатах и логическом включени/выключении насоса"""

        msg = f"p:{xyz[0]}:{xyz[1]}:{xyz[2]}:{int(pump)}#"
        print(msg)
        bytes_to_send = str.encode(msg)

        self.udp.sendto(bytes_to_send, self.server_address_port)




