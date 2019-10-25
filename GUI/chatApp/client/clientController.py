from clientUI import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class controller(QtWidgets.QMainWindow):

    def __init__(self):
        super(controller,self).__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.BtnConnect.clicked.connect(self.BtnConnectClicked)
        self.ui.BtnSend.clicked.connect(self.BtnSendClicked)

    '''Defining the functions for signals'''
    def BtnConnectClicked(self):
        self.ui.TextDebug.append("Connect Button Clicked")

    def BtnSendClicked(self):
        self.ui.TextDebug.append("Send Button Clicked")

'''Starting the Application loop'''
app = QtWidgets.QApplication([])
application = controller()
application.show()
sys.exit(app.exec_())