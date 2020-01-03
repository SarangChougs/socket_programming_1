''''This is the Model of the client side. This contains all the
Backend code of the client side of the application.'''

import socket

class Model():

    '''Constructor'''
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.clientStatus = False
        self.connectionStatus = False

    def startClient(self):
        self.s = socket.socket()
        self.clientStatus = True
        print(self.clientStatus)

    def connectToServer(self):
        try:
            self.s.connect((self.ip,self.port))
            self.connectionStatus = True
            print(">>Connection = " + self.connectionStatus)
        except ConnectionRefusedError:
            print("Server Not Started.\nPlease start Server first.")

    def sendMssg(self, mssg):
        if self.connectionStatus:
            self.mssg = mssg
            self.s.sendall(bytes(mssg,'UTF-8'))
        else:
            return

    def recvMssg(self):
        return self.s.recv(1024).decode()

def main():
    m = Model('127.0.0.1',1234)
    m.startClient()
    m.connectToServer()

if __name__ == "__main__":
    main()

