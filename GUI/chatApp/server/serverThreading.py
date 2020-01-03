from PyQt5.QtCore import *

'''This contains the server code which will run in parallel in the background'''

class ServerThread(QRunnable):
   
    def __init__(self,s):
      super().__init__()
      self.connectionStatus = 'no client connection'
      self.s = s
      self.textToSend = ""
      self.textReceived =""

    @pyqtSlot()
    def run(self):
        # accepting the client connections
        if self.connectionStatus == 'no client connection':
            print(">>Waiting for connection")
        while True:   
            self.c,self.addr = self.s.accept()
            if self.addr != '':
                self.connectionStatus = 'client connected'
                print(f'Client Connected-{self.addr}')
                while self.connectionStatus == 'client connected':
                    self.textReceived = self.c.recv(1024)
                    if(self.textReceived != ''):
                        print("Text received>>" + self.textReceived)
                    elif self.textToSend !='':
                        self.c.sendall(bytes(self.textToSend,'UTF-8'))
                        print("Text send>>" + self.textToSend)
                    else:
                        print("nothing done")
