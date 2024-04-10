import socket

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ("192.168.42.88", 8888)

states = {
    "move": "r:0:0:0:1",
    "wait":  "r:0:0:1:0",
    "error": "r:1:0:0:0",
    "auto": "r:0:1:0:0"
}

def send_pult(state: str, num_str:int, text: str):
    try:
        if (0 < num_str < 5) and  (len(text < 21)):
            msgFromClient = states[state] + ":" + str(num_str) + ":" + text
            print(msgFromClient)
            bytesToSend = str.encode(msgFromClient)
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        
        else:
            print("incorrect packet")

    except KeyboardInterrupt as e:
            print("Interrupted")
            

