import socket
import threading

HOST = '127.0.0.1'
PORT = 50030

class serverThread(threading.Thread):
    def __init__(self,conn,addr,thread_list):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        thread_list.append(self)
        self.thread_list = thread_list

    def run(self):
        while True:
            data = self.conn.recv(1024)
            print data
            if (data):
                for element in thread_list:
                    element.conn.sendall(data)
                if (data == "exit"):
                    while (len(thread_list)>0):
                        thread = thread_list.pop()
                        thread.conn.close()
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

if __name__ == '__main__':
    server_main()
