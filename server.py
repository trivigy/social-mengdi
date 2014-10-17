import socket
import threading

HOST = '127.0.0.1'
PORT = 50030

bool end_server = False
class serverThread(threading.Thread):
    def __init__(self,conn,addr,thread_list):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        thread_list.append(self)
        self.thread_list = thread_list

    def run(self):
        while True:
            print "here"
            data = self.conn.recv(1024)
            print data
            if (data):
                for element in self.thread_list:
                    element.conn.sendall(data)
                if (data == "exit"):
                    end_server = True
                    return

def server_main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    thread_list = []
    while True:
        conn,addr=s.accept()
        print addr
        if (conn):
            thread = serverThread(conn,addr,thread_list)
            thread.start()
        if (end_server):
            return
        

if __name__ == '__main__':
    server_main()
