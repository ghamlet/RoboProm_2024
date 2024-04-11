#!/usr/bin/env python3

import socket
import threading
import os, signal

def udp_socket_recv_client(udp_socket_client, recv_address):
    udp_socket_client.bind(recv_address)
    while True:
        recv_data, recv_addr = udp_socket_client.recvfrom(1024)
        print('\n')
        print('>> [Получено сообщение от <% s>]'% recv_addr[0],
                recv_data.decode('utf-8') + '\n' + '<<', end='')

def udp_socket_send_client(udp_socket_client, send_address):
    print("Ссылка успешно, вы можете отправить сообщение")
    while True:
        send_data = "gey"
        
        udp_socket_client.sendto(send_data.encode('utf-8'), send_address)

def main():
    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv_ip = "192.168.0.69"
    recv_port = 8888
    send_ip = "192.168.0.80"
    send_port = 8888
    recv_address = (recv_ip, int(recv_port))
    send_address = (send_ip, int(send_port))

    socket_send_thread = threading.Thread(target=udp_socket_send_client,
            args=(udp_socket_client, send_address)
            )
    socket_recv_thread = threading.Thread(target=udp_socket_recv_client,
            args=(udp_socket_client, recv_address)
            )
    socket_recv_thread.start()
    socket_send_thread.start()

if __name__ == '__main__':
    main()
