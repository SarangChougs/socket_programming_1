from clientUI import Ui_MainWindow
from PyQt5 import QtWidgets
from clientModel import Model
import sys

class controller(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.model = Model('127.0.0.1',1234)
        self.model.startClient()
       
    def setupUi(self,mainWindow):
        super().setupUi(mainWindow)
        self.BtnConnect.clicked.connect(self.BtnConnectClicked)
        self.BtnSend.clicked.connect(self.BtnSendClicked)
        self.TextReceiver.setText(self.Textself.model.recvMssg())
        self.TextReceiver.repaint()

    '''Defining the functions for signals'''
    def BtnConnectClicked(self):
        self.TextDebug.append("Connect Button Clicked")
        self.model.connectToServer()
        if self.model.connectionStatus:
            self.TextDebug.apppend(f"Connected to server>>(\'{self.model.ip}\',{self.model.port})")
        else:
            self.TextDebug.append('Server not Started')
        

    def BtnSendClicked(self):
        self.TextDebug.append("Send Button Clicked")
        self.model.mssg = self.LineSend.text()
        self.LineSend.setText("")
        if self.model.connectionStatus:
            self.TextReceiver.append(self.model.mssg)
            self.model.sendMssg(self.model.mssg)
        else:
            self.TextReceiver.append("Client not connect")
        self.TextReceiver.repaint()
        self.TextDebug.append("Message entered by user>>" + self.model.mssg)
        
        
'''Starting the Application loop'''
app = QtWidgets.QApplication([])
ui = controller()
mainwindow = QtWidgets.QMainWindow()
ui.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())