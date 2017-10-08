import sys
import socket
import select
# import threading
from threading import Thread

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = []

class ClientThread(Thread):
    def __init__(self, client_address, sock):
        Thread.__init__(self)
        self.client_address = client_address
        self.sock = sock

    def run(self):
        namafile = 'mytext.txt'
        file = open(namafile, 'rb')
        while True:
            data = file.read(1024)
            while (data):
                self.sock.send(data)
                print 'Isi filenya => ', repr(data)
                # print 'File berhasil dikirim'
                data = file.read(1024)
            if not data:
                file.close()
                self.sock.close()
                break

try:
    while True:
        print 'menunggu client'
        # read_ready, write_ready, exception = select.select(input_socket, [], []) ini bikin error
        (client_socket, client_address) = server_socket.accept()
        # print 'got connection from ', client_address
        print client_socket.getpeername(), ' => sedang terhubung'
        thread = ClientThread(client_address, client_socket)
        thread.start()
        input_socket.append(thread)

except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)