''''This is the Model of the client side. This contains all the
Backend code of the client side of the application.'''

import socket

class Model():

    '''Constructor'''
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.clientStatus = 'Not Started'
        self.connectionStatus = 'Not Connected'

    def startClient(self):
        self.s = socket.socket()
        self.clientStatus = 'Client started'
        print(self.clientStatus)

    def connectToServer(self):
        try:
            self.s.connect((self.ip,self.port))
            self.connectionStatus = f'Connected to server (\'{self.ip}\',{self.port})'
            print(">>" + self.connectionStatus)
        except ConnectionRefusedError:
            print("Server Not Started.\nPlease start Server first.")



def main():
    m = Model('127.0.0.1',1234)
    m.startClient()
    m.connectToServer()

if __name__ == "__main__":
    main()

