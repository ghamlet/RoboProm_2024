import socket

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ("192.168.42.10", 8888)

states = {
    "move": "l:0:0:0:1#",
    "wait":  "l:0:0:1:0#",
    "error": "l:1:0:0:0#",
    "auto": "l:0:1:0:0#"
}

def send_lamp(state):
    try:
        msgFromClient = states[state]
        print(msgFromClient)
        bytesToSend = str.encode(msgFromClient)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    except KeyboardInterrupt as e:
            print("Interrupted")

