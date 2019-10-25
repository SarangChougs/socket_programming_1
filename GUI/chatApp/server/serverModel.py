'''This class conatins the pure backend code of the application.
All the methods, variables which do not directly interact with the UI are present here.'''

import socket

class Model():

    '''Constructor'''
    def __init__(self,ip,port):
        self.ip =ip
        self.port = port
        self.s = socket.socket()
        self.serverStatus = 'Server Stopped'
        self.connectionStatus = 'No Client connected'

    def startServer(self):
        self.s.bind((self.ip,self.port))
        self.s.listen(5)
        self.serverStatus = f'Server Started at (\'{self.ip}\',{self.port})'
        print(">>" + self.serverStatus)
        # if self.connectionStatus == 'No Client connected':
        #     print(">>Waiting for connection")
        # self.c,self.addr = self.s.accept()
        # if self.addr != '':
        #     self.connectionStatus = f'Client connected - {self.addr}'
        #     print(self.connectionStatus)

    def stopServer(self):
        self.s.close()
        self.serverStatus = 'Server Stopped'

# def main():
#     m = Model('127.0.0.1',1234)
#     m.startServer()


# if __name__ == "__main__":
#     main()
