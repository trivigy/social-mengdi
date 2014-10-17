<<<<<<< HEAD


=======
import socket

HOST = '127.0.0.1'
PORT = 50020;

def server_main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        print data
        if (data):
            conn.sendall(data)
        if (data == "exit"):
            conn.close()

#127.0.0.1
>>>>>>> origin/master
if __name__ == '__main__':
    server_main()
