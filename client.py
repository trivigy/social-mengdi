# Echo client program
import socket

HOST = '127.0.0.1'
PORT = 50030;            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, worldlololl fjkdlsjlk ')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
if __name__ == '__main__':
    print "CLIENT WORKS!!!"
