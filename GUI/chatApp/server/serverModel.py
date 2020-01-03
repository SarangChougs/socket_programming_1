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
        self.s.bind((self.ip,self.port)) #binding the serverf to socket
        self.s.listen(5)    #starting the server
        self.serverStatus = f'Server Started at (\'{self.ip}\',{self.port})'
        print(">>" + self.serverStatus)

