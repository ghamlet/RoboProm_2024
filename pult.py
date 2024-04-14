import socket

class Pult:
    
    def __init__(self, server_address_port):
        self.server_address_port = server_address_port
        self.udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    def send_pult(self, state: str, num_str: int, text: str):
        try:
            if (0 < num_str < 5) and (len(text) < 21):
                msg_from_client = self.states[state] + ":" + str(num_str - 1) + ":" + text + "#"
                print(msg_from_client)
                bytes_to_send = str.encode(msg_from_client)
                self.udp.sendto(bytes_to_send, self.server_address_port)

            else:
                print("incorrect packet")

        except KeyboardInterrupt as e:
            print("Interrupted")

    states = {
        "move": "r:0:0:1:0",
        "wait": "r:0:0:0:1",
        "error": "r:1:0:0:0",
        "auto": "r:0:1:0:0",
        "stop": "r:0:0:0:0"
    }

