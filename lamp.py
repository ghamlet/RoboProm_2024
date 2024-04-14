import socket

class Lamp:
    def __init__(self, server_address_port):
        self.server_address_port = server_address_port
        self.udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def send_lamp(self, state):
        try:
            msg_from_client = self.states[state]
            print(msg_from_client)
            bytes_to_send = str.encode(msg_from_client)
            self.udp.sendto(bytes_to_send, self.server_address_port)
        except KeyboardInterrupt as e:
            print("Interrupted")

    states = {
        "move": "l:0:0:1:0#",  # green
        "wait": "l:0:0:1:0#",  # yellow
        "error": "l:1:0:0:0#",  # red
        "auto": "l:0:1:0:0#",  # blue
        "stop": "l:0:0:0:0#"
    }


