import socket
import sys
import select

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
	with open('file_diterima', 'wb') as file:
		print 'file terbuka'

		while True:
			data = client_socket.recv(1024)
			print(data)
			# message = sys.stdin.readline()
			# client_socket.send(message)
			file.write(data)

			if not data:
				file.close()
				print 'file close()'
				break			

except KeyboardInterrupt:
	client_socket.close()
	sys.exit(0)