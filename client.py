<<<<<<< HEAD
import socket
import cmd

class Main(cmd.Cmd):
    def preloop(self):
        self.prompt = "#-> "
        self.HOST = '127.0.0.1'
        self.PORT = 50020
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))

    def do_send(self, msg):
        self.socket.sendall(msg)
        data = self.socket.recv(1024)
        if data:
            print data
        
        
    def do_exit(self, line):
        self.socket.close()
        return True


=======
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
>>>>>>> origin/master
if __name__ == '__main__':
    main = Main()
    try:
        main.cmdloop()
    except KeyboardInterrupt:
        main.echo("")
        main.onecmd("exit")

# def main():
#     
#     
#     
#     totalsent = 0
#     while totalsent < len(msg):
#         sent = self.sock.send(msg[totalsent:])
#         if sent == 0:
#             raise RuntimeError("socket connection broken")
#         totalsent = totalsent + sent
# 
# if __name__ == '__main__':
#     main()
