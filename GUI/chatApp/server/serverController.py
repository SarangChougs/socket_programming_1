from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from serverUI import Ui_MainWindow
from serverModel import Model
from serverThreading import ServerThread
import sys

'''This is the controller of the server side program.
This contains the Controller class which inherits the serverUI class.
This also contains the main funciton which is the starting point of the application'''

class Controller(Ui_MainWindow):

    '''Constructor'''
    def __init__(self):
        super().__init__() #initialising the super class
        self.model = Model('127.0.0.1',1236)
        self.threadpool = QThreadPool() #initialising a seperate thread for starting server in the background

    '''SetUp the UI of the super class, 
    add here the code that relates to 
    the way UI works'''
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.splitter.setSizes([300,0])
        self.BtnStart.clicked.connect(self.BtnStartClicked)
        self.BtnSend.clicked.connect(self.BtnSendClicked)    

    def BtnStartClicked(self):
        serverTh = ServerThread(self.model.s) # object of the serverThread class
        self.model.startServer()
        self.threadpool.start(serverTh) #starting the thread
        self.TextDebug.append("Start Button Clicked")
        self.TextDebug.append(self.model.serverStatus)
        self.BtnStart.setDisabled(True)

    def BtnSendClicked(self):
        self.TextDebug.append("Send Button Clicked")
        self.TextSender.append(self.LineSend.text())
        self.TextSender.repaint()
        self.LineSend.setText("")

'''The main entry point of the application'''
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  #reference to QMainWindow qt widget
    ui = Controller()  #object of the controller class
    ui.setupUi(MainWindow) #setupUI method ot the UI class
    MainWindow.show()  #starting the main window
    sys.exit(app.exec_()) #closing the window when user ends it
    ui.model.s.close()
main()