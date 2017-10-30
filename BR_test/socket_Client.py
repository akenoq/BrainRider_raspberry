import sys
import threading
import requests
import random
import json
import time
import socket
import logging

# version 3 : работает с socket_Server.py
class BrainClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8081
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        self.data = "111"

    # send data to port
    def send_data(self, message):
        self.sock.send(message.encode())
        self.data = self.sock.recv(1024)
        print('Received from server: ' + self.data.decode())

if __name__ == '__main__':

    client = BrainClient()

    def send_data_to_sock(message):
        client.send_data(message)

    while True:
        message = input(" -> ")
        if (message != 'q'):
            send_data_to_sock(message)
        else:
            client.sock.close()
            print('closed')
            break

# version 2 : работает с socket_Server.py
# def Main():
#
#     my_socket = socket.socket()
#     host = '127.0.0.1'
#     port = 9090
#     my_socket.connect((host, port))
#
#     message = input(" -> ")
#
#     while message != 'q':
#         my_socket.send(message.encode())
#         data = my_socket.recv(1024).decode('utf-8')
#
#         print('Received from server: ' + data)
#
#         message = input(" -> ")
#
#     my_socket.close()
#
#
# if __name__ == '__main__':
#     Main()


################################################
# version 1
# url = 'http://localhost:5555/'
# url = 'https://brainrider.herokuapp.com/datawriter'
#
# i = 0
# while True:
#     i += 1
#     course = random.choice(["Forward", "Backward", "Left", "Right"])
#     data = {
#         "id": i,
#         "data": course
#     }
#
#     req = requests.post(url, json=data)
#
#     time.sleep(15)
