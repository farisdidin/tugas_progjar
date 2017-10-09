import socket
import sys
import select

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


try:
	while True:
		message = sys.stdin.readline()
		file =  message.split(' ')
		data = file[1]
		
		client_socket.send(data)
		masuk = client_socket.recv(1024)
		#print masuk
		# file = open('data_masuk.txt', 'wb')
		# while True:
		# 	acc, addr = client_socket.accept()
		# 	bina = acc.recv(1024)
		# 	print bina
		# 	while (bina):
		# 		file.write(bina)
		# 		bina = acc.recv(1024)
		# 	file.close()
except KeyboardInterrupt:
	client_socket.close()
	sys.exit(0)