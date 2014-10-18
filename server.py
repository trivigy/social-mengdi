import socket
import threading

HOST = '127.0.0.1'
PORT = 50030

class serverThread(threading.Thread):
    def __init__(self,conn,addr,thread_list, s_server):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.s_server = s_server
        thread_list.append(self)
        self.thread_list = thread_list
        self.kill = False

    def run(self):
        while not self.kill:
            data = self.conn.recv(1024)
            print data
            if (data):
                for element in self.thread_list:
                    element.conn.sendall(data)
                if (data == "exit"):
                    for element in self.thread_list:
                        element.kill = True
                    self.s_server.shutdown(socket.SHUT_RDWR)

def server_main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    thread_list = []
    
    while True:
        print "HAZA"
        try:
            conn, addr = s.accept()
            print addr
            if (conn):
                thread = serverThread(conn, addr, thread_list, s)
                thread.start()
        except:
            break
        

if __name__ == '__main__':
    server_main()
