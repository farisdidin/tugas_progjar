import socket
import sys
import select

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


try:
	while True:
		message = sys.stdin.readline()
		client_socket.send(message)
		
except KeyboardInterrupt:
	client_socket.close()
	sys.exit(0)