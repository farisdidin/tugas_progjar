import socket
import threading

server_address = ('', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)