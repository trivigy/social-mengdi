import socket
import threading
import cmd
import signal

class Client(threading.Thread):
    def __init__(self, prog):
        threading.Thread.__init__(self)
        self.prog = prog
        self.kill = False

    def run(self):
        while not self.kill:
            data = self.prog.socket.recv(1024)
            if data:
                self.prog.onecmd("print " + data)
                if data == "exit":
                    self.kill = True

class Main(cmd.Cmd):
    def preloop(self):
        self.prompt = "#-> "
        self.HOST = '127.0.0.1'
        self.PORT = 50030

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))

        Client(self).start()

    def do_send(self, msg):
        self.socket.sendall(msg)

    def do_print(self, msg):
        print ""
        print msg

    def do_exit(self, line):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    main = Main()
    try:
        main.cmdloop()
    except:
        pass


